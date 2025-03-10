from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer, TaskUpdateSerializer
# Create your views here.
# views = python functions or classes that process incoming web requests and return responses
# urls are mapped to views
# ViewSets combine the logic of multiple related operations/views (get,post,put,..) into a single class

class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for hanling Task CRUD operations"""
    # query all objects 
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        "Return appropriate serializer class based on request method"
        if self.action =='create':
            return TaskCreateSerializer
        elif self.action in ['update','partial_update']:
            return TaskUpdateSerializer
        return TaskSerializer
    
    # define what is returned to user
    def get_queryset(self):
        # filter queryset based on query parameters
        queryset = Task.objects.all()
        
        #  Filter by completion status if provided, None otherwise
        completed = self.request.query_params.get('completed',None)
        if completed is not None:
            completed = completed.lower()=='true' # convert TRUE param to True boolean
            queryset = queryset.filter(completed=completed) # return fields with condition 
        return queryset
        
            

    
    