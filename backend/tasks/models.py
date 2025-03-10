from django.db import models # models module from django provides classes and methods to define models
import uuid

# Create your models here.
class Task(models.Model):
    """Model representing a task in the system"""
    
    # Define fields (columns of DB Table)
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # unique id field that is the primary key and by default is unique id, not editable
    title       = models.CharField(max_length=200, db_index=True) # title of task max 200 chars db_index added for quick lookups by title
    description = models.TextField(blank=True, null=True) # text field, can be blank and null?
    priority    = models.IntegerField(default=1)
    completed   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    # Special class to define metadata for the model (options and behaviors for model that don't directly relate to fields)
    class Meta:
        ordering = ['-created_at'] # default order for task when they are retrieved from database (minus means descending)
    # str method defines string representation of the task
    def __str__(self) -> str:
        return self.title
    
    