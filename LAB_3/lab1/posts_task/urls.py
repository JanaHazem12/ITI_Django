from django.urls import path
from .views import index, PostsList, ModifyPost, AuthorsList, ModifyAuthor



urlpatterns = [
    # path('', views.index, name="index"),
    # path('', views.index, name="index"),
    path('posts/', PostsList.as_view(), name='posts_list'),
    path('posts/<int:pk>', ModifyPost.as_view(), name='modify_post'),
    path('authors/', AuthorsList.as_view(), name='authors'),
    path('authors/<int:pk>', ModifyAuthor.as_view(), name='modify_author'),
    # path('<str:post>/', views.dictionary, name='postsDict'),
    # path('author/<int:author>', views.authorInfo, name='authorInfo'),
]
