from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
    path('',views.Mains,name='main'),
    path('home/', views.Movies_List, name='movies_list'),
    path('movie/<int:pk>/', views.Movie_Details, name='movie_details'),
    path('rentedmovie/<int:pk>/', views.Rented_Details, name='rented_details'),
    path('home/',views.Home,name='home'),
    path('allmovies/',views.All_Movies,name='allmovies'),
    path('userview/',views.User_View,name='userview'),
    path('rented/',views.Rented,name='rented'),
    path('rented/success/',views.RentedSuccessView,name='rentedsuccess'),
    path('signup/', views.Sign_Up , name='signup'),
    path('search/',views.SearchMovies, name='searchmovies'),
    path('email/', views.Email_View, name='email'),
    path('success/', views.Success_View, name='success'),
    path('watch/', views.Watch,name='watch'),
    path('rent/<int:pk>/', views.rent, name='rent'),


]
