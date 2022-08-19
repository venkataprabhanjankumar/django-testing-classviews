from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.DemoView.as_view()),
    path('sucess', views.FeedBackSucess.as_view()),
    path('register', views.Register.as_view()),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signin', views.Login.as_view(), name='signin'),
    path('createpost', views.CreatePost.as_view(), name='create_post'),
    path('viewposts', views.DisplayPosts.as_view(), name='list_posts'),
    path('deletepost/<int:pk>', views.DeletePost.as_view(), name='delete_post'),
    path('updatepost/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    path('createbook', views.create_book, name='create_book'),
    path('view_post/<int:pk>', views.ViewPost.as_view(), name='view_post')
]
