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
    path('single_hood/<hood_id>', views.single_neighborhood, name='single-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),

]