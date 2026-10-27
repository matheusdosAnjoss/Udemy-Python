from django.urls import path

from home import views as home_views
from blog import views as blog_views


urlpatterns = [
    path('', home_views.home),
]