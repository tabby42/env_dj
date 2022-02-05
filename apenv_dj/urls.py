from django.urls import path
from .views import sunny_day_delete, sunny_day_list, sunny_day_single, index


urlpatterns = [
    path('', index, name='index'),
    path('sunny_days/', sunny_day_list, name='sunny_days'),
    path('sunny_days/<int:id>/', sunny_day_single, name='singlesunny_day'),
    path('sunny_days/<int:id>/delete/', sunny_day_delete)
]



