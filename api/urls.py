from django.urls import path
from . import views
urlpatterns = [
    path('events', views.get_all_envents, name='get_events'),
    path('create', views.create_event, name='create_event')
]
