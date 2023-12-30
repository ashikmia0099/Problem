from django import forms
from .models import Post_model,Comment_model

class postForm(forms.ModelForm):
    class Meta:
        model = Post_model
        # fields = '__all__'
        exclude=['author']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_model
        fields = ['name','email','comment',]