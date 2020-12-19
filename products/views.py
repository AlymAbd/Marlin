from django.views.generic import TemplateView
from products.models import Products

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

# Create your views here.
