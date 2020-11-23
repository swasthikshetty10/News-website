
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.article, name='article'),
    path('cities', views.cities, name='cities'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('sports', views.sports, name='sports'),
    path('lifestyle', views.lifestyle, name='lifestyle'),


]