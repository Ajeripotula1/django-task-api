from django.urls import path, include # used for defining URL patterns in Django
from rest_framework.routers import DefaultRouter # DRF utility that automatically generates API routes for ViewSets
from .views import TaskViewSet

# create a router to automatically generate API endpoints for our viewset
router = DefaultRouter()
router.register(r'tasks', TaskViewSet) # map tasks TaskViewSet to /tasks/ endpoint

# the API urls are now determined automatically by the router

urlpatterns = [
    path('',include(router.urls))
]
