from django.urls import path
from .views import goal_delete, goal_list, goal_single, index, remind


urlpatterns = [
    path('', index, name='index'),
    path('goals/', goal_list, name='goals'),
    path('goals/<int:id>/', goal_single, name='singlegoal'),
    path('goals/<int:id>/delete/', goal_delete)
]

urlpatterns += [
    path('goals/<int:id>/remind/', remind, name='remind'),
]

