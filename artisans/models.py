from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=48)
    official_name = models.CharField(max_length=128)
    currency = models.CharField(max_length=48)
    languages = models.CharField(max_length=256)
    timezones = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_all(cls):
        return Country.objects.all()

    @classmethod
    def get_name(cls, name):
        return Country.objects.get(name=name)

class Artisan(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=48)
    company = models.CharField(max_length=48)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, related_name="artisan")
    identifier = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"

    @classmethod
    def get_all(cls):
        return Artisan.objects.all()

    @classmethod
    def get_id(cls, id):
        return Artisan.objects.get(id=id)

class ArtisanInfo(models.Model):
    artisan = models.OneToOneField(Artisan, on_delete=models.CASCADE, related_name="artisanInfo")
    id_number = models.CharField(max_length=48, null=True, blank=True)
    marital_status = models.CharField(max_length=48, null=True, blank=True)
    number_of_children = models.IntegerField(null=True, blank=True)
    working_hours = models.IntegerField(null=True, blank=True)
    religion = models.CharField(max_length=48, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.artisan.first_name}, {self.artisan.last_name}"