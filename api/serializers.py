from rest_framework import serializers
from .models import Event, FireAndIce


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'date')

class FireAndIce(serializers.ModelSerializer):
    class Meta:
        model = FireAndIce
        fields = ('emoji', 'date')
