from django.http import HttpResponse
from django.shortcuts import render
from cooking.models import  Recipe

# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')


def index_view(request, *args, **kwargs):
    name = request.GET.get('username', '') \
           or request.POST.get('username') \
           or 'world'
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(
        request,
        template_name='index.html',
        context={
            'context_name': name,
            'recipes': recipes
        }
    )
