from .views import FetchHotels
from django.urls import path

urlpatterns = [
    path('list/', FetchHotels.as_view()),
]