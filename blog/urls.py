from blog.views import PostListView
from django.urls import path
from . import views

app_name = 'blog'
# this is application namespace, this allows us to organize URLs by application and use the name when referring to them

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    # The above int and slug parameters are called as path converters
    # The name parameter allows us to name the URL project-wide.

]