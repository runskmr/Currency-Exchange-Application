from django.urls import path
from CADConversion import views

urlpatterns = [
    path('', views.CADConversion, name='CADConversion'),
    path('', views.USDConversion, name='USDConversion'),
    # path('americandollar', views.americandollar)
    
]