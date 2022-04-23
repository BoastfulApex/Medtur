from django.db import models
from django.contrib.postgres.fields import ArrayField


class Locations(models.Model):
    location = models.CharField(max_length=120, null=True, blank=True)
    location_photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.location


class Clinics(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    vertify = models.BooleanField(default=False)
    services = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    open_date = models.TimeField(auto_now_add=False, null=True, blank=True)
    close_date = models.TimeField(auto_now_add=False, null=True, blank=True)
    rate = models.FloatField(default=0)
    booking = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        if self.photo.url:
            return self.photo.url
        else:
            return ''


class Services(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    photo = models.ImageField(null=True)

    def __str(self):
        return self.name

    @property
    def ImageURL(self):
        if self.photo.url:
            return self.photo.url
        else:
            return ''


class Tours(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    cost = models.PositiveIntegerField(default=0)
    where = models.ForeignKey(Locations, on_delete=models.CASCADE)
    duration_day = models.PositiveIntegerField(default=0)
    duration_night = models.PositiveIntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Queries(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(unique=False, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    query = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Rates(models.Model):
    rate = models.PositiveIntegerField(null=True, blank=True)
    clinic = models.ForeignKey(Clinics, on_delete=models.CASCADE)


class Specialist(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    specialities = models.CharField(max_length=120, null=True, blank=True)
    photo = models.ImageField(null=True)
    clinic = models.ForeignKey(Clinics, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now_add=False, null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Stories(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now_add=False, null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

