from django.urls import path
from . import views

app_name = 'penjualan'

urlpatterns = [
    path('tabel/', views.get_all_mymodels, name='read'),
    path('create/', views.create_mymodel, name='create'),
    path('update/<str:kdjual>/', views.update_mymodel, name='update'),
    path('delete/<str:kdjual>/', views.delete_mymodel, name='delete'),
]
