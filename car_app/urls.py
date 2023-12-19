
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.CarDetails.as_view(), name="details"),
    path('create_order/<int:id>/', views.create_order, name="create_order"),
    path('add_car/', views.add_car, name="add_car"),
    path('add_brand/', views.add_brand, name="add_brand"),
    path('filter_brand/<int:id>/', views.filter_brand, name="filter_brand")
]
