from typing import Any
from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy



# Class Based View Create section
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post_model
    form_class = forms.postForm
    template_name = 'post.html'
    success_url = reverse_lazy('postpage')
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)



# Class Based View Edit section

@method_decorator(login_required, name='dispatch')

class EditPostView(UpdateView):
    model = models.Post_model
    form_class = forms.postForm
    template_name = 'post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')




# Class Based View Delete section
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post_model
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
    
    
# class DetailPostView(DetailView):
#     model = models.Post_model
#     pk_url_kwarg = 'id'
#     template_name = 'post_details.html'
    
#     def get_context_data(self, **kwargs:):
        
        