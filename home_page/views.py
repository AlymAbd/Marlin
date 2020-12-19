from django.shortcuts import render
from django.http import HttpResponse
from products.models import Categories as ProductGroups
from django.views.generic import TemplateView, View
# Create your views here.

class homepage(TemplateView):
    template_name='home_page/home.html'

    def get_context_data(self, **kwargs):
        groups = ProductGroups.objects.filter(is_active=True, is_category=True).values('id', 'name', 'parent__name')

        gr_agg = {}
        for group in groups:
            parent = group['parent__name']
            gr_agg[parent] = [{'name': x['name'], 'id':x['id']} for x in groups if x['parent__name']==parent]

        context = super().get_context_data(**kwargs)
        context['groups'] = gr_agg
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
