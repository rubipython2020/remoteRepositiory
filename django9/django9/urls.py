"""django9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from institute import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('Cources/',views.Cources,name='Cources'),
    path('list/',views.courselist,name='courselist'),

    path('register/',views.registration,name='register'),
    path('feedback/',views.feed,name='feedback'),
    path('readd/',views.readd,name='readd'),
    path('enquari/',views.enquairy_view,name='enquari'),
    path('entry/',views.Entry,name='entrystudent'),
    path('',views.student , name='student'),
    path('update/<id>/',views.update_form,name='update'),
    path('update_form_save/<id>/',views.update_form_save,name='update_form_save'),
    path('delete/<id>',views.delete,name='delete')

]
