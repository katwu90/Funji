from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Flower


def index(request):
    all_flowers = Flower.objects.all()
    return render(request, 'flowers/index.html', {'all_flowers': all_flowers})

def detail(request, flower_id):
	flower = get_object_or_404(Flower, pk=flower_id)
	return render(request, 'flowers/details.html', {'flower': flower})

def cart(request, flower_id):
	selected_flower = get_object_or_404(Flower, pk=flower_id)
	selected_flower.in_cart = True
	selected_flower.save()
	return render(request, 'flowers/details.html', {'flower': flower})

	# try:
	# 	selected_flower = flower.get(pk=request.POST['flower'])
	# except (KeyError, Flower.DoesNotExist):
	# 	return render(request, 'flowers/index.html', {
	# 		'flower': flower,
	# 		'error_message': "This flower does not exist!"
	# 		})
	# else:
	# 	