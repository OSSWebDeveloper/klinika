from django.urls import path
from . import views

urlpatterns = [

    # ru

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('doktors', views.doktors, name='doktors'),
    path('doktors/<int:id>', views.doktor_detail, name='doktor_detail'),
    path('xizmatlar', views.xizmatlar, name='xizmatlar'),
    path('xizmatlar/<int:id>', views.xizmat_detail, name='xizmat_detail'),
    path('galereya', views.galereyaru, name='galereyaru'),

    # uz

    path('uz/', views.indexuz, name='indexuz'),
    path('uz/contact', views.contactuz, name='contactuz'),
    path('uz/doktors', views.doktorsuz, name='doktorsuz'),
    path('uz/doktors/<int:id>', views.doktor_detailuz, name='doktor_detailuz'),
    path('uz/xizmatlar', views.xizmatlaruz, name='xizmatlaruz'),
    path('uz/xizmatlar/<int:id>', views.xizmat_detailuz, name='xizmat_detailuz'),
    path('uz/galereya', views.galereya, name='galereya'),

]

