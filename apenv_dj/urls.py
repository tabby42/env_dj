from django.urls import path
from .views import sunny_day_list, sunny_day_single, index, signup_request, edit_request, SunshineCreateView, SunshineUpdateView, SunshineDeleteView



urlpatterns = [
    path('', index, name='index'),
    path('sunny_days/', sunny_day_list, name='sunny_days'),
    path('sunny_days/<int:id>/', sunny_day_single, name='singlesunny_day'),
    path("sunny_days/signup/", signup_request, name="signup"),
    path("sunny_days/edit/<int:id>", edit_request, name="edit")
]

urlpatterns += [
    path('sunny_days/create/', SunshineCreateView.as_view(), name='sunshine-create'),
    path('sunny_days/<int:pk>/update/', SunshineUpdateView.as_view(), name='sunshine-update'),
    path('sunny_days/<int:pk>/delete/', SunshineDeleteView.as_view(), name='sunshine-delete'),
]



