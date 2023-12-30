from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Post_model(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='posts/media/uploads/',blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Comment_model(models.Model):
    post = models.ForeignKey(Post_model, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add =True)
    
    def __str__(self) -> str:
        return f'Comments by {self.name}'
    
    