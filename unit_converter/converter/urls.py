from django.urls import path
from .views import length_conversion, weight_conversion, temperature_conversion, home

from django.shortcuts import redirect

def base(request):
    return redirect('home')


urlpatterns = [
    path('length/', length_conversion, name='length_conversion'),
    path('weight/', weight_conversion, name='weight_conversion'),
    path('temperature/', temperature_conversion, name='temperature_conversion'),
    path('', home, name='home'),

]
