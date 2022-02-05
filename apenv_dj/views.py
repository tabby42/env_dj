from django.shortcuts import render
from .models import Goal
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    num_goals = Goal.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_goals': num_goals,
        'num_visits': num_visits
    }
    return render(request, 'index.html', context)

@login_required
def goal_list(request):
    goal = Goal.objects.filter(user=request.user)
    paginator = Paginator(goal, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
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
