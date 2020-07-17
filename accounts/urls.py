from django.contrib.auth.views import LogoutView
from django.urls import path, include
from accounts import views

urlpatterns = [
    # path('', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
