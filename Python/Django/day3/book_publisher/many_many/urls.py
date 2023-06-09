from django.urls import path, include



from . import views

urlpatterns = [
    path('',views.index),
    path('add_book',views.create_book),
    path('add_publisher',views.create_publisher),
    path('connection',views.connection),
]