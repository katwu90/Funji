from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Flower

def index(request):
	all_flowers = Flower.objects.all()
	return render(request, 'flowers/index.html', {'all_flowers': all_flowers})

def detail(request, flower_id):
	flower = get_object_or_404(Flower, pk=flower_id)
	return render(request, 'flowers/details.html', {'flower': flower})