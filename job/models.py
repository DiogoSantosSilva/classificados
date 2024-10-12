
from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    class Meta:
        db_table = "job"
        
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    workers = models.ManyToManyField(User, related_name='jobs')
