import email
from django.shortcuts import render, redirect
from .models import Sunshine
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import datetime
from django import forms
#from .widgets import BootstrapDateTimePickerInput
from .forms import NewUserForm, UpdateUserForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.contrib import messages

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
    paginator = Paginator(sunny_day, 5)
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

def signup_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("sunny_days")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "sunny_day/signup.html", context={"signup_form":form})

@login_required
def edit_request(request, id):
    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated." )
            return redirect('edit', id=id)
        messages.error(request, "Update was unsuccessful. Invalid information.")
    item = get_object_or_404(User, id=id)
    form = UpdateUserForm(
        initial={
            'id': item.id,
            'username': item.username, 
            'first_name': item.first_name,
            'last_name': item.last_name,
            'email': item.email
    })
    return render(request, 'sunny_day/edit_profile.html', context={'edit_form': form})

class SunshineCreateView(CreateView):
    model = Sunshine
    fields = ['date', 'sunbeam_1', 'sunbeam_2', 'sunbeam_3', 'is_completed']
    success_url = reverse_lazy('sunny_days')

    def form_valid(self, form):
        sunshine = form.save(commit=False)
        sunshine.user = User.objects.get(username=self.request.user) 
        sunshine.save()
        return super(SunshineCreateView, self).form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None: 
            form_class = self.get_form_class()
        form = super(SunshineCreateView, self).get_form(form_class)
        input_formats=['%d.%m.%Y']
        form.fields['date'].widget = forms.DateInput(format='%d.%m.%Y')
        return form

class SunshineUpdateView(UpdateView):
    model = Sunshine
    fields = ['date', 'sunbeam_1', 'sunbeam_2', 'sunbeam_3', 'is_completed']   
    success_url = reverse_lazy('sunny_days')

    def form_valid(self, form):
        sunshine = form.save(commit=False)
        sunshine.user = User.objects.get(username=self.request.user) 
        sunshine.save()
        return super(SunshineUpdateView, self).form_valid(form)

class SunshineDeleteView(DeleteView):
    model = Sunshine
    success_url = reverse_lazy('sunny_days')
