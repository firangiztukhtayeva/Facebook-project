from django.urls import path
from .views import post_view,post_detail,home_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('posts/', post_view, name='post_view'),
    path('posts/<slug:slug>/', post_detail, name='post_detail')
]
