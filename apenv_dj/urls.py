from django.urls import path
from .views import goal_delete, goal_list, goal_single, index


urlpatterns = [
    path('', index, name='index'),
    path('goals/', goal_list, name='goals'),
    path('goals/<id>/', goal_single, name='singlegoal'),
    path('goals/<id>/delete/', goal_delete, name='deletegoal')
]