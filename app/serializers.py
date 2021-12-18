from rest_framework import serializers
from .models import Hotel, Hours

class HourSerializer(serializers.RelatedField):

    def to_representation(self, value):
        data = {
            value.day : {
                'opens_at' : value.opens_at,
                'closes_at' : value.closes_at
            }
        }
        return data

    class Meta:
        model = Hours
        fields = ['day', 'opens_at', 'closes_at']

class HotelSerializer(serializers.ModelSerializer):
    operating_hours = HourSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = ['uid','name','operating_hours']