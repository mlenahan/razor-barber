from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_overview, name='blog_overview'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blog-reply-edit/<int:reply_id>/', views.blog_reply_edit,
         name='blog_reply_edit'),
    path('delete-confirmation/<int:reply_id>/',
         views.blog_reply_confirm_delete,
         name='blog_reply_confirm_delete'),
    path('blog-reply-delete/<int:reply_id>/', views.blog_reply_delete,
         name='blog_reply_delete'),
]
