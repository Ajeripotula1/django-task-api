from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task

class Command(BaseCommand):
    help = "Create users and tasks for testing"
    def handle(self,*args, **kwargs):
        # create users
        user2 = User.objects.create_user(username="user2",email="user2@gmail.com",password="user2")
        user2.first_name = 'John'
        user2.last_name = 'Doe'
        user2.save()
        
        self.stdout.write(self.style.SUCCESS("User created successfully!"))
        
        #create task for user1
        task1 = Task.objects.create(title="Task1", description="descr", user=user2)
        self.stdout.write(self.style.SUCCESS("Tasks created successfully!"))
