from django.db import models


class Job(models.Model):
    class Meta:
        db_table = "job"
    title = models.CharField(max_length=255)