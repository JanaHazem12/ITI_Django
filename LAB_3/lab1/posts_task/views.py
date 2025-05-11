from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.loader import get_template
from rest_framework import generics
from rest_framework.response import Response
from .models import Author, Post, Comment
from .serializers import PostSerializer, AuthorSerializer


# Create your views here.
class PostsList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class ModifyPost(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class AuthorsList(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class ModifyAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer


# posts_dict = {
#     "First Post": {
#         "content": "Hello world! Welcome to my blog.",
#         "author": "user1",
#         "image": "images/first_image.jpeg"
#     },
#     "Second Post": {
#         "content": "List comprehensions are faster than for loops.",
#         "author": "user2",
#         "image": "images/second_image.webp"
#     },
#     "Third Post": {
#         "content": "Learn how to create a Django project in 5 minutes.",
#         "author": "user1",
#         "image": "images/third_image.jpeg"
#     },
#     "Fourth Post": {
#         "content": "Always write clean and maintainable code.",
#         "author": "user3",
#         "image": "images/fourth_image.jpeg"
#     }
# }



def index(request):
    return HttpResponse("Welcome to our HomePage !")

# # def dictionary(request, post):
#     # use pk instead of post
#     # post_data = posts_dict[post]
#     # return render(request, "posts_task/post_content.html", context={
#     # 'post_data': post_data})
#     all_posts = Post.objects.get(id=post)
#     posts_comment = Comment.objects.filter(post_id=post)
#     # use related_name instead of this query ^
#     # post.comments.all in html
#     return render(request, "posts_task/post_content.html", context={
#         'post': all_posts,
#         'posts_comment': posts_comment
#     })

# # def read(request):
#     # posts = [{"title": title, "image": post_data["image"]} for title, post_data in posts_dict.items()]
#     return render(request, "posts_task/index.html", context={
#         # 'all_posts': posts,
#         'post': Post.objects.all()
#     })

# # # def authorInfo(request, author):
# #     all_authors = Author.objects.get(id=author)
# #     post_author = Post.objects.filter(author_id=author)
# #     # use author.posts.all instead of this query^
# #     posts_number = post_author.aggregate(count=Count('id'))
# #     # use related_name for this query too ^ - post_author.posts.count()/length
# #     return render(request,  "posts_task/author_info.html", context={
# #         'author': all_authors,
# #         'posts_by_author': post_author,
# #         'posts_number': posts_number
# #     })    