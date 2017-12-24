# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Flower

def index(request):
	all_flowers = Flower.objects.all()
	template = loader.get_template('flowers/index.html')
	context = {
		'all_flowers': all_flowers,
	}
	return HttpResponse(template.render(context, request))

def detail(request, flower_id):
	return HttpResponse("<h2>Details for flower:" + str(flower_id) + "</h2>")

