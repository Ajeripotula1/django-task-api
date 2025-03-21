from django.urls import path, include # used for defining URL patterns in Django
# from rest_framework.routers import DefaultRouter # DRF utility that automatically generates API routes for ViewSets
from .views import TaskListCreateView, TaskDetailView
from uuid import UUID

# # create a router to automatically generate API endpoints for our viewset
# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet) # map tasks TaskViewSet to /tasks/ endpoint

# the API urls are now determined automatically by the router

urlpatterns = [
    # map our endpoint to view
    path('', TaskListCreateView.as_view(), name ='task-list-create'),
    path('<uuid:id>/',TaskDetailView.as_view(), name='detailed-task-operations')
]
