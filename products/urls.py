from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:categoryid>', views.ProductInCategory.as_view())
]