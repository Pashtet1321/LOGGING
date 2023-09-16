from django.urls import path
from .views import (
    ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, subscriptions, IndexView
)

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', cache_page(60*10)(ProductDetail.as_view()), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('go/', IndexView.as_view())

]