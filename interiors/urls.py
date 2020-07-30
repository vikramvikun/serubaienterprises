from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('services',views.services,name="services"),
    path('works',views.works,name="works"),
    path('contact',views.contact,name="contact"),
    path('service/<str:value>',views.service),
    path('work/<str:val>',views.work),
    path('login',views.login),
    path('logout',views.logout),
]