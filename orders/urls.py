from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_order, name='user_order'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete/<int:item_id>/', views.delete_order_item, name='delete_order_item'),
]