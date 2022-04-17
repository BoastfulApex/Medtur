from rest_framework import routers
from medturApp.views import *

router = routers.DefaultRouter()

router.register(r'locations', LocationView, basename="locations")
router.register(r'tours', TourView, basename="tours")
router.register(r'clinics', ClinicView, basename="clinics")
router.register(r'services', ServiceView, basename="services")
router.register(r'queries', QueryView, basename="queries")
router.register(r'rates', RateView, basename="rates")
router.register(r'news', NewsView, basename="news")
router.register(r'stories', StoriesView, basename="stories")

