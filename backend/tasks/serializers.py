# Serializer for Task model: convert complex data types like the Django model instance to python
# data types easily rendered into JSON, can also handle deserialization
# make it easy to send Task Model data as JSON and validate incoming JSON data b4 saving to database
# once you create instance of model, you can pass it to a defined serializer to get data in JSON format
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # define which model fields are exposed in the API response
        fields = ['id', 'title', 'description', 'priority', 'completed', 'created_at', 'updated_at']
        # auto generated, cannot be modified by API users
        read_only_fields = ['id', 'created_at','updated_at']
    
    # custom validation method 
    def validate_priority(self,value):
        """Validate that priority is between 1 and 5"""
        if value < 1 or value > 5:
            raise serializers.ValidationError("Priority must be between 1 and 5")
        return value

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title','description','priority','completed']

    def validate_priority(self,value):
        """Validate that priority is between 1 and 5"""
        if value < 1 or value > 5:
            raise serializers.ValidationError("Priority must be between 1 and 5")
        return value

class TaskUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating tasks"""
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'completed']
        extra_kwargs = {
            'title': {'required':False},
            'description': {'required': False},
            'priority': {'required': False},
            'completed': {'required': False}
        }

    def validate_priority(self,value):
        """Validate that priority is between 1 and 5"""
        if value < 1 or value > 5:
            raise serializers.ValidationError("Priority must be between 1 and 5")
        return value

        