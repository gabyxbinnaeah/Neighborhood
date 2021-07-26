from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns =[
    path('',views.index, name='index'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profile, name="profile"),
    path('edit/',views.edit_profile,name='edit'),
    path('newhood/',views.create_neighborhood, name="newhood"),
    path('singlehood/<hood_id>',views.single_neighborhood, name='singlehood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
    path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
    # url(r'^singlehood/(\d+)/$',views.single_neighborhood, name='singlehood')
]