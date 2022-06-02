from django.urls import path
from products.views import product_detail_view,product_create_view,product_delete_view,product_list_view,people_update_view
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:id>/', product_detail_view, name='detail'),
    path('create/', product_create_view, name='create'),
    path('delete/<int:id>/', product_delete_view, name='delete'),
    path('<int:id>/update/', people_update_view, name='people-update'),
    
]
