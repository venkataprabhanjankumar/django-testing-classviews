from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, include, reverse
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView, ListView, UpdateView, DeleteView
from django.conf import settings
from decorators.check_login import check_login
from decorators.auth import check_user
from mixins.LoginCheckMixin import LoginCheckMixin
from django.views.generic.detail import SingleObjectMixin, DetailView

from .models import User, Post
from .forms import SignUp, Demo, SignIn, PostForm, BookForm


class FeedBackSucess(View):
    def dispatch(self, request, *args, **kwargs):
        return render(request, 'sucess_page.html')


class DemoView(FormView):
    form_class = Demo
    template_name = 'demo.html'
    success_url = '/user/sucess'

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data.get('message'))
        form.send_email()
        return super().form_valid(form)


class Register(CreateView):
    model = User
    form_class = SignUp
    template_name = 'signup.html'
    success_url = '/user/dashboard'


class Login(FormView):
    template_name = 'login.html'
    form_class = SignIn
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return render(self.request, 'login.html', {'err': 'Invalid Credentials', 'form': form})
        else:

            login(request=self.request, user=user)
            return super().form_valid(form)


# @check_login
@check_user(login_url='/user/signin')
def dashboard(request):
    return render(request, 'dashboard.html')


class CreatePost(LoginCheckMixin, CreateView):
    template_name = 'create_post.html'
    model = Post
    login_url = reverse_lazy('signin')
    success_url = reverse_lazy('list_posts')
    # form_class = PostForm
    # if we specify form_class we can not specify fields attribute
    # forms_class and fields cannot be used together
    fields = ['post_name', 'post_description']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user.username
        post.save()
        return super(CreatePost, self).form_valid(form)


class DisplayPosts(LoginCheckMixin, ListView):
    model = Post
    template_name = 'list_posts.html'
    context_object_name = 'posts'
    login_url = '/user/signin'

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)


class UpdatePost(LoginCheckMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    login_url = reverse_lazy('signin')

    def get_success_url(self):
        return reverse('update_post', kwargs={'pk': self.kwargs['pk']})


class DeletePost(LoginCheckMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')
    login_url = reverse_lazy('signin')
    template_name = 'delete_post.html'


@check_login
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user.username
            book.save()
            return redirect(reverse_lazy('view_books'))
    else:
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})


class ViewPost(LoginCheckMixin, SingleObjectMixin, ListView):
    # we cannot use detail view here
    template_name = 'view_post.html'
    model = Post
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request,'view_post.html',{'post': self.object})

