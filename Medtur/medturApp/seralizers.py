from .models import *
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinics
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = '__all__'


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = '__all__'


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'
