from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone

from .forms import SolicitudForm
from .models import Solicitud

# Create your views here.

def index(request):
    #return HttpResponse("Index")
    return render(request, 'solicitud/index.html')

class SolicitudList(ListView):
    model = Solicitud
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']=timezone.now()
        return context

class SolicitudCreate(CreateView):
    template_name = 'solicitud/s_form.html'
    form_class = SolicitudForm
    success_url = '/solicitud/lista/'

    def form_valid(self, form):
        return super().form_valid(form)

class SolicitudEditar(UpdateView):
    model = Solicitud
    template_name = 'solicitud/s_form.html'
    form_class = SolicitudForm
    success_url = '/solicitud/lista/'

    def form_valid(self, form):
        return super().form_valid(form)

class SolicitudEliminar(DeleteView):
    model = Solicitud
    template_name = 'solicitud/s_delete.html'
    form_class = SolicitudForm
    success_url = '/solicitud/lista/'

    # def form_valid(self, form):
    #     return super().form_valid(form)