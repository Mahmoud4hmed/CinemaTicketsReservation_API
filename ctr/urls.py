from django.contrib import admin
from django.urls import path
from tickets import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/fbv/', views.FBV_List),
    path('rest/fbv/<int:pk>/', views.FBV_pk),
]
