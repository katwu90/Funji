from django.views import generic
from .models import Flower

class IndexView(generic.ListView):
    template_name = 'flowers/index.html'
    context_object_name = 'all_flowers'

    def get_queryset(self):
        return Flower.objects.all()

class DetailView(generic.DetailView):
    model = Flower
    template_name = 'flowers/details.html'

