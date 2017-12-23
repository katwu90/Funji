# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the flowers home page</h1>")

def detail(request, flower_id):
	return HttpResponse("<h2>Details for flower:" + str(flower_id) + "</h2>")

