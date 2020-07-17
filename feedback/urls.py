from django.urls import path
from feedback import views

urlpatterns = [
    path('create', views.create, name="create"),
    path('success', views.success, name='success')
]
