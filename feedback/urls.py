from django.urls import path
from feedback import views

urlpatterns = [
    path('feedback/create', views.create, name="create"),
    path('feedback/success', views.success, name='success'),
    path('', views.create)
]
