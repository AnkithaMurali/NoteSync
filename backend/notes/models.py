from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class Version(models.Model):
    note = models.ForeignKey(Note, related_name='versions', on_delete=models.CASCADE)
    content = models.TextField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    change_diff = models.JSONField(default=dict)



