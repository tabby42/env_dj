from django.shortcuts import render
from .models import Goal
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    num_goals = Goal.objects.all().count()
    context = {
        'num_goals': num_goals
    }
    return render(request, 'index.html', context)

def goal_list(request):
    goal = Goal.objects.all()
    context = {
        'goal_list': goal
    }
    return render(request, 'goal/goal_list.html', context )

def goal_single(request, id):
    goal_single = Goal.objects.get(id = id)
    context = {
        'goal_single': goal_single
    }
    return render(request, 'goal/goal_single.html', context)

def goal_delete(request, id):
    goal_del = Goal.objects.get(id = id)
    goal_del.delete()
    return HttpResponseRedirect('/goals/')
