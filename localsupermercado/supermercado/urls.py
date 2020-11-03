from django.urls import path
from . import views

urlpatterns =[

path('',views.index,name='index'),

path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name="cliente-detail"),
path('clientes/',views.ClienteListView.as_view(),name='clientes'),
]

urlpatterns+=[
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),

    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),

    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    
    
]