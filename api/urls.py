from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'', views.EventViewSet)
router.register(r'', views.FireAndIceViewSet)

urlpatterns = [
    path('fireandice', views.get_fire_or_ice, name='get_fire_or_ice'),
    path('events', include(router.urls), name='get_events'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-get-token/', obtain_auth_token, name='gettoken'),
]
