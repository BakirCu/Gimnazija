from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='lekcije-home'),
    path('prvi_razred/', views.prvi_razred, name='prvi-razred'),
    path('drugi_razred/', views.drugi_razred, name='drugi-razred'),
    path('treci_razred/', views.treci_razred, name='treci-razred'),
    path('cetvrti_razred/', views.cetvrti_razred, name='cetvrti-razred'),
    path('lekcija/<str:id>/', views.lekcija, name='lekcija'),
    path('lekcije/<str:godina>/', views.lekcije_godine, name='lekcije_godine'),
    path('video/<str:id>/', views.video, name='video'),
    path('predmet/<str:predmet>/<str:godina>/', views.predmet, name='predmet'),
    path('prvi-razred-prijava', views.prvi_razred_prijava,
         name='prvi-razred-prijava'),
]
