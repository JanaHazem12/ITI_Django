from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.loader import get_template



# Create your views here.

posts_dict = {
    "First Post": {
        "content": "Hello world! Welcome to my blog.",
        "author": "user1",
        "image": "images/first_image.jpeg"
    },
    "Second Post": {
        "content": "List comprehensions are faster than for loops.",
        "author": "user2",
        "image": "images/second_image.webp"
    },
    "Third Post": {
        "content": "Learn how to create a Django project in 5 minutes.",
        "author": "user1",
        "image": "images/third_image.jpeg"
    },
    "Fourth Post": {
        "content": "Always write clean and maintainable code.",
        "author": "user3",
        "image": "images/fourth_image.jpeg"
    }
}



def index(request):
    return HttpResponse("Welcome to our HomePage !")

def dictionary(request, post):
    post_data = posts_dict[post]
    return render(request, "posts_task/post_content.html", context={
    'post_data': post_data})
    # make a template for this ^

def read(request):
    # posts = list(posts_dict.keys()) # posts number to loop on it
    posts = [{"title": title, "image": post_data["image"]} for title, post_data in posts_dict.items()]
    return render(request, "posts_task/index.html", context={
        # 'post_data':posts_dict[post],
        # 'post':post,
        # 'post_dict': posts_dict,
        'all_posts': posts,
        'test':"TESTING"
    })