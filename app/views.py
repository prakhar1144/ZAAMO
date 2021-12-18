from rest_framework.generics import ListAPIView
from .models import Hotel
from .serializers import HotelSerializer

class FetchHotels(ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        queryset = Hotel.objects.filter(type=self.request.query_params.get('type'))
        return queryset