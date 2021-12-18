import requests
from datetime import datetime
from app.models import Hotel, Hours


def addOperatingHours(hotel, data):
    hours = []
    for k in data["hours"]:
        opens_at = datetime.strptime(data["hours"][k]['opens_at'], "%H:%M %p").time()
        closes_at = datetime.strptime(data["hours"][k]['closes_at'], "%H:%M %p").time()
        h = Hours(day=k,opens_at=opens_at,closes_at=closes_at)
        h.save()
        hours.append(h)
    hotel.operating_hours.add(*hours)


for i in range(10):
    data = requests.get("https://random-data-api.com/api/restaurant/random_restaurant").json()
    hotel = Hotel(uid=data["uid"], name=data["name"], type=data["type"])
    hotel.save()
    addOperatingHours(hotel, data)
    