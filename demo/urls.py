from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('path1', views.ViewDemo.as_view(), name='view1'),
    path('path2', views.ViewDemo2.as_view(), name='view2'),
    path('path3', views.TemplateDemo.as_view(), name='view3'),
    path('about', TemplateView.as_view(template_name='about.html', extra_context={'message': "Hii"})),
    path('about1', views.AboutPage.as_view()),
    path('books', views.BooksDemo.as_view()),
    path('books1', views.BooksDemo1.as_view(), name='view_books'),
    path('books2', views.BooksDemo2.as_view()),
    path('books3/<int:pk>', views.BooksDemo3.as_view()),  # variable name must be pk
    path('books4/<int:pk>', views.BooksDemo4.as_view()),
    path('books5',views.BooksDemo5.as_view()),
    path('books6/<int:pk>',views.BooksDemo6.as_view())
]
