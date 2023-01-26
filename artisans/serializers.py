import imp
from rest_framework import serializers

from .models import Artisan, ArtisanInfo, Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            "id",
            "name",
            "official_name",
            "currency",
            "languages",
            "timezones",
        )

class ArtisanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtisanInfo
        fields = (
            "id_number",
            "marital_status",
            "number_of_children",
            "working_hours",
            "religion",
        )

class ArtisanSerializer(serializers.ModelSerializer):
    artisanInfo = ArtisanInfoSerializer(many=False,)
    country = CountrySerializer(many=False, )
    class Meta:
        model = Artisan
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'job_title',
            'company',
            'country',
            'artisanInfo',
        )