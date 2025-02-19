
from django.contrib import admin
from django.urls import path
from dishapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),

]
