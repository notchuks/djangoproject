from django.contrib import admin
from . models import GoalStatus, ScrumyHistory, ScrumyGoals

admin.site.register(GoalStatus)
admin.site.register(ScrumyHistory)
admin.site.register(ScrumyGoals)

# Register your models here.
