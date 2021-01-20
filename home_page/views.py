from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from products import models

# Create your views here.

class homepage(TemplateView):
    template_name='home_page/home.html'

    def get_context_data(self, **kwargs):
        groups = models.Categories.objects.filter(is_active=True, is_category=True).values('id', 'name', 'parent__name')

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
        from django.db.models import Count
        product_count = models.Products.objects.filter(is_active = True).annotate(count_pr = Count("pk"))
        group_count = models.Groups.objects.filter(is_category = False, is_active = True).annotate(count_pr = Count("pk"))
        categories_count = models.Groups.objects.filter(is_category = True, is_active = True).annotate(count_pr = Count("pk"))
        
        context = super().get_context_data(**kwargs)
        context['products'] = len(product_count)
        context['groups'] = len(group_count)
        context['categories'] = len(categories_count)

        return context


class contacts(TemplateView):
    template_name = 'home_page/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


