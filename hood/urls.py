from . import views
from django.urls import path

urlpatterns =[
    path('',views.index, name='index'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profile, name="profile"),
    path('edit/',views.edit_profile,name='edit'),
    path('newhood/',views.create_neighborhood, name="newhood"),
]