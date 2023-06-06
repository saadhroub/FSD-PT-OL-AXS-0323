from django.urls import path, include

from . import views

urlpatterns = [
    path('/<name>', views.index),
    path('process', views.form_process),
    path('success', views.success),
    path('logreg', views.sign_up),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method),
    
    ]