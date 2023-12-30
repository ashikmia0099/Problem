from django.urls import path,include
from . import views
urlpatterns = [
    # path('post/',views.Post,name='postpage'),
    path('post/',views.AddPostCreateView.as_view(), name='postpage'),
    # path('edit/<int:id>',views.Edit,name='editpage'),
    path('edit/<int:id>',views.EditPostView.as_view(),name='editpage'),
    # path('delete/<int:id>',views.DeletePage,name='deletepage'),
    path('delete/<int:id>/sure',views.DeletePostView.as_view(),name='deletepage'),
    # path('detials/<int:id>/',views.DetailPostView.as_view(),name='detialpage')
    
]