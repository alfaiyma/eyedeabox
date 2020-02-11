from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('refresh', views.onDBRefresh, name="refresh"),
    path('about', views.aboutView, name="about"),
    path('contact', views.contactView, name="contact")
]