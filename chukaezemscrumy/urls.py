from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.index),
    path('goal/', views.index1),
    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal/', views.add_goal),
    path('home/', views.home),
]