# from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# authentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task
from .serializers import TaskSerializer
from uuid import UUID

# Create your views here.
# views = python functions or classes that process incoming web requests and return responses
# urls are mapped to views
# ViewSets combine the logic of multiple related operations/views (get,post,put,..) into a single class

class TaskListCreateView(views.APIView):
    """ View deals with Multiple (all) tasks. List all tasks and create a new one"""
    
    # require authentication)_classes for this view
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        """
        GET /tasks/ -> Return all tasks created by user
        GET /tasks/?completed=true -> Return all tasks or filter by completed status
        """
        # query all model objects (entries)
        tasks = Task.objects.filter(user=request.user)
        
        # extract the query parameter (params in the URL), set it to None if none provided
        completed = request.query_params.get('completed', None)
        
        # handle filtering logic
        if completed is not None:
            # if completed.lower() == true, completed = True, False otherwise 
            completed = completed.lower() == 'true'
            completed = tasks.filter(completed=completed)
        
        # return Python obj tasks to user as JSON
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        '''POST /tasks/ -> create a new Task '''
        # user serializer to deserialize (validate and extract data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # save vlaidated data to dataset
            serializer.save(user=request.user) # need to specify the user (foreign key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailView(views.APIView):
    '''Handles retrieving (GET), updating (PUT/PATCH), and deleting (DELETE) based on ID'''  
    
    def get(self, request, id):
        '''GET /task/ -> Retrieves task based on id (primary key)'''
        # print(id, type(id))
        # cat = UUID(id)
        # print(cat)
        task = get_object_or_404 (Task,id=id) # queries from Task model for entry with id=url param
        serializer = TaskSerializer(task) # serialize task into JSON
        return Response(serializer.data)
    
    def patch(self,request, id):
        '''PUT tasks/<int:id>'''
        
        task = get_object_or_404(Task,id=id)
        # pass exisiting model instance, and data u want to update 
        serializer = TaskSerializer(task,data=request.data, partial=True) # serialize new/upated data JSON Data -> Py
        # validate updated data
        if serializer.is_valid():
            # save if is, dont otw
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        '''DELETE tasks/<int:id>'''
        task = get_object_or_404(Task,id=id) # get task to make sure it exists
        task.delete() # delete the object
        return Response(status=status.HTTP_204_NO_CONTENT)





# class TaskViewSet(viewsets.ModelViewSet):
#     """ViewSet for hanling Task CRUD operations"""
#     # query all objects 
#     queryset = Task.objects.all()
    
#     def get_serializer_class(self):
#         "Return appropriate serializer class based on request method"
#         if self.action =='create':
#             return TaskCreateSerializer
#         elif self.action in ['update','partial_update']:
#             return TaskUpdateSerializer
#         return TaskSerializer
    
#     # define what is returned to user
#     def get_queryset(self):
#         # filter queryset based on query parameters
#         queryset = Task.objects.all()
        
#         #  Filter by completion status if provided, None otherwise
#         completed = self.request.query_params.get('completed',None)
#         if completed is not None:
#             completed = completed.lower()=='true' # convert TRUE param to True boolean
#             queryset = queryset.filter(completed=completed) # return fields with condition 
#         return queryset
        
            

    
    