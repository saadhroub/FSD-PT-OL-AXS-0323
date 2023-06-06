from django.urls import path, include

from . import views

urlpatterns = [
    path('/<name>', views.index),
    path('process', views.form_process),
    path('success', views.success),
    path('logreg', views.sign_up),
   
    ]