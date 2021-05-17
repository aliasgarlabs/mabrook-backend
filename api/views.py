from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Create your views here.
@api_view(['GET'])
def get_all_envents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


def create_event(request):
    if request.method == 'POST':
        title = request.REQUEST.get('title')
        date = datetime.strptime(request.REQUEST.get('date'), '%d-%m-%Y')
        event = Event.objects.create(title=title, date=date)
        return HttpResponse(status=201, content=f"{event.title} event was created")
    else:
        return HttpResponse(status=404, content='error')
