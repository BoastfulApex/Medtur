from django.shortcuts import render
from .seralizers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class LocationView(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer


class TourView(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer


class ClinicView(viewsets.ModelViewSet):
    queryset = Clinics.objects.all().order_by('-rate')
    serializer_class = ClinicSerializer

    def retrieve(self, request, *args, **kwargs):
        clinic_id = kwargs['pk']
        clinic = self.queryset.get(id=clinic_id)
        services = []
        for service_id in clinic.services:
            ser = Services.objects.get(id=service_id)
            service = {
                'id': ser.id,
                'name': ser.name,
                'photo': ser.ImageURL,
            }
            services.append(service)
        clinics = {
            'name': clinic.name,
            'location': clinic.location.id,
            'photo': clinic.ImageURL,
            'services': services,
            'open_date': clinic.open_date,
            'close_date': clinic.close_date,
            'rate': clinic.rate,
        }
        return Response({"clinic": clinics})


class ServiceView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        cli = []
        clinics = Clinics.objects.filter(services__overlap=[f'{id}'])
        service1 = self.queryset.get(id=id)
        for clinic in clinics:
            cl = {
                'id': clinic.id,
                'name': clinic.name,
                'location': clinic.location.id,
                'photo': clinic.ImageURL,
                'services': clinic.services,
                'open_date': clinic.open_date,
                'close_date': clinic.close_date,
                'rate': clinic.rate,
            }
            cli.append(cl)
        service = {
            'id': service1.id,
            'name': service1.name,
            'photo': service1.ImageURL,
            'clinics': cli,
        }
        return Response({'data': service})


class QueryView(viewsets.ModelViewSet):
    queryset = Queries.objects.all()
    serializer_class = QuerySerializer


class RateView(viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            print(data)
            clinic_id = data['clinic'].id
            clinic = Clinics.objects.get(id=clinic_id)
            rate = Rates.objects.create(
                rate=data['rate'],
                clinic=clinic
            )
            rate.save()
            r = 0
            rate = 0
            rates = Rates.objects.filter(clinic_id=clinic_id)
            for i in rates:
                rate += i.rate
                r += 1
            rate = rate / r
            clinic.rate = rate
            clinic.save()
            return Response({"status": 'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class StoriesView(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StorySerializer
