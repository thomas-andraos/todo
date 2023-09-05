from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #if user is deleted task deletes too
    title = models.CharField(max_length=200) #Title max length 200 chars not null or blank
    description = models.TextField(null=True, blank=True) #Textfield can be null and blank
    complete = models.BooleanField(default=False) #Auto set to false (bool val)
    created = models.DateTimeField(auto_now_add=True) #Auto set to dateTime of creation

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] #ordering query set