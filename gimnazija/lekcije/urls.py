from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lekcije-home'),
    path('prvi_razred/', views.prvi_razred, name='prvi-razred'),
    path('drugi_razred/', views.drugi_razred, name='drugi-razred'),
    path('trci_razred/', views.treci_razred, name='treci-razred'),
    path('cetvrti_razred/', views.cetvrti_razred, name='cetvrti-razred'),
    path('predmet/', views.predmet, name='predmet'),
    path('predmet/<int:id>', views.predmet, name='predmet'),
]
