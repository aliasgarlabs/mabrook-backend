from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Event, FireAndIce
from .serializers import EventSerializer, FireAndIceSerializer
from rest_framework import viewsets
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class FireAndIceViewSet(viewsets.ModelViewSet):
    queryset = FireAndIce.objects.all()
    serializer_class = FireAndIceSerializer


# Create your views here.
@api_view(['GET'])
def get_all_envents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

    # Create your views here.
@api_view(['GET'])
def get_fire_or_ice(request):
    fire_or_ice = FireAndIce.objects.latest('date')

    serializer = FireAndIceSerializer(fire_or_ice)
    return Response(serializer.data)


def create_event(request):
    if request.method == 'POST':
        title = request.REQUEST.get('title')
        date = datetime.strptime(request.REQUEST.get('date'), '%d-%m-%Y')
        event = Event.objects.create(title=title, date=date)
        return HttpResponse(status=201, content=f"{event.title} event was created")
    else:
        return HttpResponse(status=404, content='error')
