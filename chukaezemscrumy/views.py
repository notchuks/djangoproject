from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User
from random import randint

def index(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id = goal_id)
    return HttpResponse(goal.goal_name)

def add_goal(request):
    myuser = User.objects.get(username = 'louis')
    mygoalstatus = GoalStatus.objects.get(status_name = 'Weekly Goal')
    record = ScrumyGoals.objects.create( goal_name = 'Keep Learning Django', goal_id = str(randint(1000, 9999)),
    created_by = 'Louis', moved_by = 'Louis', owner = 'Louis', goal_status = mygoalstatus, user = myuser)

def home(request):
    ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(ScrumyGoals.goal_name)

# Create your views here.
