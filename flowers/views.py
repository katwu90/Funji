# Create your views here.
from django.http import HttpResponse
from .models import Flower

def index(request):
	all_flowers = Flower.objects.all()
	html = ''
	for flower in all_flowers:
		url = '/flowers/' + str(flower.id)
		html += '<a href="' + url + '">' + flower.name + '</a><br>'
	return HttpResponse(html)

def detail(request, flower_id):
	return HttpResponse("<h2>Details for flower:" + str(flower_id) + "</h2>")

