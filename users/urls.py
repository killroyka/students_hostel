from django.urls import path

import users.views as views

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name="login")
    ]
