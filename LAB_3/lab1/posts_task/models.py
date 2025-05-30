from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)    
    phone_number = models.CharField(max_length=20)
    # models.CharField(max_length=40) - better for phone_number
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Post(models.Model):
    title = models.CharField(max_length=60)
    # image_url = models.CharField(max_length=200, null=True, blank=True)    
    content = models.TextField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=200)
    posted_by = models.CharField(max_length=80) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"comment by: {self.posted_by}"