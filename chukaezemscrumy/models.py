from django.db import models
from django.contrib.auth.models import User

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=50)

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT, related_name='goalstatus')
    user = models.ForeignKey(User, related_name='scrumygoals', on_delete = models.PROTECT)

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.IntegerField()
    goal = models.ForeignKey(ScrumyGoals, on_delete = models.PROTECT, related_name='scrumygoals')


# Create your models here.
