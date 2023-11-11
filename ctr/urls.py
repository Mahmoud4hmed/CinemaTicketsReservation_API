from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/fbv/', views.FBV_List),
    path('rest/fbv/<int:pk>/', views.FBV_pk),
    path('rest/cbv/', views.CBV_List.as_view()),
    path('rest/cbv/<int:pk>/', views.CBV_pk.as_view()),
    path('fbv/findmovie/', views.find_movie),
    path('fbv/newreservation/', views.new_reservation),
    path('fbv/reservations/', views.reservation_list),
    path('rest/generics/', views.generics_list.as_view()),
    path('rest/generics/<int:pk>/', views.generics_pk.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
