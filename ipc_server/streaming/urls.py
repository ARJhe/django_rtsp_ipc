from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='streaming_home'),
]