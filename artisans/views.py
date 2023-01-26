import requests
from datetime import datetime
from multiprocessing.spawn import import_main_path
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Artisan, ArtisanInfo, Country
from .serializers import ArtisanSerializer

def get_country_info(country_name):
    country = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    country_info = {"status":country.status_code}
    print(country.json())
    if country.status_code == 200:
        country_info["official_name"] = country.json()[0]["name"]["official"]
        for one, two in country.json()[0]["currencies"].items():
            country_info["currency"] = f"{one}: {two['name']}"
            break
        country_info["languages"] = ", ".join([f"{one}: {two}" for one, two in country.json()[0]["languages"].items()])
        country_info["timezones"] = ", ".join([one for one in country.json()[0]["timezones"]])
        country_info["status"] = 200
        print(country_info)
    return country_info


# Create your views here.
class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = Artisan.get_all()
    serializer_class = ArtisanSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        print(request.data)
        try:
            country = Country.get_name(request.data["country"])
        except:
            resp = get_country_info(request.data["country"])
            if resp["status"] == 200:
                country = Country()
                country.name = request.data["country"]
                country.official_name = resp["official_name"]
                country.languages = resp["languages"]
                country.timezones = resp["timezones"]
                country.currency = resp["currency"]
                country.save()
            else:
                return Response({"message":"Unable to get country info","status":resp["status"]}, status=status.HTTP_400_BAD_REQUEST)

        if request.data["id"] in [0, "0"]:
            artisan = Artisan()
        else:
            try:
                artisan = Artisan.get_id(request.data["id"])
            except:
                artisan = Artisan()
        artisan.first_name = request.data["first_name"]
        artisan.last_name = request.data["last_name"]
        artisan.date_of_birth = datetime.strptime(request.data["date_of_birth"].split("T")[0], '%Y-%m-%d')
        artisan.job_title = request.data["job_title"]
        artisan.company = request.data["company"]
        artisan.country = country
        artisan.identifier = f'{request.data["first_name"]}{request.data["last_name"]}{request.data["date_of_birth"].split("T")[0].replace("-","")}'
        artisan.save()
        try:
            artisanInfo = artisan.artisanInfo
        except:
            artisanInfo = ArtisanInfo(artisan=artisan)
            artisanInfo.save()
        if request.data["country"] == "Kenya":
            artisan.artisanInfo.id_number = request.data["id_number"]
            artisan.artisanInfo.marital_status = request.data["marital_status"]
        elif request.data["country"] == "Uganda":
            artisan.artisanInfo.number_of_children = request.data["number_of_children"]
            artisan.artisanInfo.marital_status = request.data["marital_status"]
        elif request.data["country"] == "Tanzania":
            artisan.artisanInfo.working_hours = request.data["working_hours"]
            artisan.artisanInfo.religion = request.data["religion"]
        artisan.artisanInfo.save()
        return Response({"message":"Created successfully", "status":200}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            "message":"Deleted successfully",
            "status":200,
            "artisans":ArtisanSerializer(Artisan.get_all(), many=True).data
        }, status=status.HTTP_200_OK)