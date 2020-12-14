from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
# Create your views here.

class homepage(TemplateView):
    template_name='home_page/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class about(TemplateView):
    template_name = 'home_page/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class contacts(TemplateView):
    template_name = 'home_page/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
