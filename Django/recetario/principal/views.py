from principal.models import Receta
from principal.forms import ContactoForm, RecetaForm, ComentarioForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.core import serializers

def index(request):
    recetas = Receta.objects.all()
    return render_to_response(
        'index.html',
        {'recetas': recetas},
        context_instance=RequestContext(request)
    )


def nueva_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RecetaForm()
    return render_to_response(
        'nueva_receta.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ComentarioForm()
    return render_to_response(
        'comentario.html',
        {'form': form},
        context_instance=RequestContext(request)
    )



def usuarios(request):
    usuarios = User.objects.all()
    return render_to_response(
        'usuarios.html',
        {'usuarios': usuarios},
        context_instance=RequestContext(request)
    )


def detalle_receta(request, id):
    receta = get_object_or_404(Receta, pk=id)
    return render_to_response(
        'detalle_receta.html',
        {'receta': receta},
        context_instance=RequestContext(request)
    )


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = "Mensaje desde el recetario."
            contenido = formulario.cleaned_data["mensaje"] + "\n"
            contenido += "Comunicarse a: " + formulario.cleaned_data["correo"]
            correo = EmailMessage(titulo, contenido, to=["rajiv.rivero@gmail.com"])
            correo.send()
            return HttpResponseRedirect("/")
    else:
        formulario = ContactoForm()
    return render_to_response(
        "contactoform.html",
        {'formulario': formulario},
        context_instance=RequestContext(request)
    )


def ajax(request):
    if request.is_ajax():
        data = serializers.serialize("json", Receta.objects.all())
        return HttpResponse(data, mimetype="application/javascript")
    else:
        return HttpResponse(status=404)
