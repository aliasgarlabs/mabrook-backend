from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Event
from datetime import datetime
import json


# Create your views here.
def get_all_envents(request):
    if request.method == 'GET':
        events = Event.objects.all()
        events_dict = {
            'events': []
        }
        for event in events:
            events_dict['events'].append({'title': event.title, 'date': event.date.strftime("%d-%m-%Y")})

        return JsonResponse(events_dict, status=200, safe=False)
    else:
        return HttpResponse(status=404, content="Error No Route Found")


def create_event(request):
    if request.method == 'POST':
        title = request.REQUEST.get('title')
        date = datetime.strptime(request.REQUEST.get('date'), '%d-%m-%Y')
        event = Event.objects.create(title=title, date=date)
        return HttpResponse(status=201, content=f"{event.title} event was created")
    else:
        return HttpResponse(status=404, content='error')
