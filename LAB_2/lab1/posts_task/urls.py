from django.urls import path
from . import views



urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.read, name="index"),
    path('<str:post>/', views.dictionary, name='postsDict'),
    path('author/<int:author>', views.authorInfo, name='authorInfo'),
]
