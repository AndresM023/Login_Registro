from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from Iniciar_sesion.models import Login_Regist
from Iniciar_sesion.forms import Registro
# Create your views here.

# class LoginView(CreateView):
#     model = Login
#     template_name = 'login.html'
#     form_class = Logeo
#     success_url = reverse_lazy('claveolv')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['action_save'] = self.request.path
#         return context


class RegistroView(CreateView):
    models = Login_Regist
    template_name = 'registro.html'
    form_class = Registro
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        return context


class LoginView(CreateView):
    models = Login_Regist
    form_class = Registro
    template_name = 'login.html'


class ClaveOlvidView(TemplateView):
    template_name = 'clave_olvidada.html'


class CodigoView(TemplateView):
    template_name = 'codigo_verificacion.html'


class ClaveNueView(TemplateView):
    template_name = 'clave_nueva.html'
