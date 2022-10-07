from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/update',views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete',views.ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/arts/new/', views.ArtCreate.as_view(), name="art_create"),
    path('category/<int:pk>/arts/<int:art_pk>/', views.CategoryArtAssoc.as_view(), name="playlist_art_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
