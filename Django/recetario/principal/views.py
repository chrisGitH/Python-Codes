from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    recetas = Receta.objects.all()
    return render_to_response('index.html', {'recetas': recetas})

def usuarios(request):
    users = User.objects.all()
    recipes = Receta.objects.all()
    return render_to_response('usuarios.html', {'users': users, 'recipes': recipes})