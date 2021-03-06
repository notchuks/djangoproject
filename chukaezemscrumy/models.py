from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField(default=1)
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT)
    user = models.ForeignKey(User, related_name='goal_created', on_delete = models.PROTECT)

    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateField()
    goal = models.ForeignKey(ScrumyGoals, on_delete = models.CASCADE)

    def __str__(self):
        return self.created_by


# Create your models here.
