# blog/urls.py

from django.urls import path
from .views import CreateBlogPost
from .views import CreateComment
from .views import ListBlogPosts
from .views import ListComments
from .views import UpdateBlogPost

urlpatterns = [
    path('create/', CreateBlogPost.as_view(), name='create-blog-post'),
    path('<int:post_id>/create-comment/', CreateComment.as_view(), name='create-comment'),
    path('list/', ListBlogPosts.as_view(), name='list-blog-posts'),
    path('<int:post_id>/list-comments/', ListComments.as_view(), name='list-comments'),
    path('<int:post_id>/update/', UpdateBlogPost.as_view(), name='update-blog-post'),

]
