from django.urls import path
from . import views 


urlpatterns = [
   path('registro/', views.registro, name="registro"),
   path('login/', views.login, name="login"),
   path('logout/', views.logout, name="logout"),
   path('active/<uidb64>/<token>/', views.activate, name='activate'),
]
