from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    recetas = Receta.objects.all()
    return render_to_response('index.html', {'recetas': recetas}, context_instance = RequestContext(request))

def usuarios(request):
    usuarios = User.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuarios}, context_instance = RequestContext(request))

def detalle_receta(request, id):
    receta = get_object_or_404(Receta, pk = id)
    return render_to_response('detalle_receta.html', {'receta': receta}, context_instance = RequestContext(request))