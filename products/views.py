from django.views.generic import TemplateView
from products.models import Products
from products import models
from rest_framework.decorators import api_view
from django.http import JsonResponse


class ProductInCategory(TemplateView):
    template_name = 'products/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cat_id = kwargs.get('categoryid')
        products = Products.objects.filter(
                            productsgroups__group__pk=cat_id, 
                            is_active=True,
                            prices__state__in=['active', 'discount']
                        ).values(
                            'id', 
                            'name', 
                            'description', 
                            'image', 
                            'prices__curr',
                            'prices__sale_price',
                            'prices__state'
                        )

        context['products'] = products
        return context


class products_list(TemplateView):
    template_name = 'products/products_list.html'

    def get_context_data(self, **kwargs):
        
        prod_list = models.Products.objects.filter(is_active = True).values(
            'name', 'id', 'description', 'prices__purchase_price', 
            'prices__sale_price', 'image'
        )
        context = super().get_context_data(**kwargs)
        context['prod_list'] = prod_list

        return context


class products_info(TemplateView):
    template_name = 'products/products_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@api_view(['GET'])    
def get_products_info(request):
    query = request.query_params
    product_id = query.get('id_product')
    product = models.Products.objects.filter(pk = product_id).values(
        'name', 'id', 'description', 'prices__purchase_price', 
        'prices__sale_price', 'image'
    )
    return JsonResponse({'product' : list(product)})
