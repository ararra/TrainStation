from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from workoutplan.models import Mesocycle

# Create your views here.

class HomepageView(ListView):
    model = Mesocycle
    template_name = 'home.html'