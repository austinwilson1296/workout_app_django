from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template import loader,TemplateDoesNotExist
from .equipment_list import *
import random
# Create your views here.


def index(request):
    return render(request,'workout_app/index.html')

def about(request):
    return render(request,'workout_app/about.html')

def price(request):
    return render(request,'workout_app/pricing.html')

def workout(request):
    context = generate_workout()
    return render(request,'workout_app/workout_creator.html',context=context)

def experience_level(request, level):
    # Create the template name based on the level
    template_name = f'workout_app/partials/experience_level_{level}.html'
    context = {
        'level':level,
        'items':gym_equipment
    }
    # Attempt to render the template
    return render(request, template_name,context)


def generate_equipment_list(request):
    if request == "GET":
        context = {
            gym_equipment:'items'
        }
    return()
