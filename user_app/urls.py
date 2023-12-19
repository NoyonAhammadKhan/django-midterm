from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/<int:id>/', views.UserProfile.as_view(), name="profile"),

]
