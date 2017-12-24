from django.http import Http404
from django.shortcuts import render
from .models import Flower

def index(request):
	all_flowers = Flower.objects.all()
	return render(request, 'flowers/index.html', {'all_flowers': all_flowers})

def detail(request, flower_id):
	try:
		flower = Flower.objects.get(pk=flower_id)
	except Flower.DoesNotExist:
		raise Http404("Flower does not exist")
	return render(request, 'flowers/details.html', {'flower': flower})