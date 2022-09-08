from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [

    #Index
    path('',index,name="index"),
    path('register', user_register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_login, name='logout'),


    # For Blog
    path('blog/create', blog_create, name='blog_create'),
    path('blog', blogs_read, name='blogs'),
    path('blog/<int:pk>/details', blog_details, name='blog_details'),
    path('blog/<int:pk>/update', blog_update, name='blog_update'),
    path('blog/<int:pk>/delete', blog_delete, name='blog_delete'),

    #For Comment
    path('blog/<int:pk>/comment', comment, name='comment'),
    path('comment/<int:pk>/delete', comment_delete, name='comment_delete'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

