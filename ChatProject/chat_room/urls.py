from django.urls import path, include
from . import views


urlpatterns = [
    path('room/', views.Rooms.as_view()),
    path('dialog/', views.Dialog.as_view()),
]