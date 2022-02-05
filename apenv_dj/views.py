from django.shortcuts import render
from .models import Sunshine
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    num_sunny_days = Sunshine.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_sunny_days': num_sunny_days,
        'num_visits': num_visits
    }
    return render(request, 'index.html', context)

@login_required
def sunny_day_list(request):
    sunny_day = Sunshine.objects.filter(user=request.user)
    paginator = Paginator(sunny_day, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'sunny_day/sunny_day_list.html', context )

def sunny_day_single(request, id):
    sunny_day_single = Sunshine.objects.get(id = id)
    context = {
        'sunny_day_single': sunny_day_single
    }
    return render(request, 'sunny_day/sunny_day_single.html', context)

def sunny_day_delete(request, id):
    sunny_day_del = Sunshine.objects.get(id = id)
    sunny_day_del.delete()
    return HttpResponseRedirect('/sunny_days/')
