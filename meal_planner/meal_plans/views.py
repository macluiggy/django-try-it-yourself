from django.shortcuts import render

# Create your views here.

def index(req):
  """The home page for meal_plans"""
  return render(req, 'meal_plans/index.html')