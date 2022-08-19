from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book


class BooksDemo(ListView):
    model = Book
    template_name = 'books.html'


class BooksDemo1(ListView):
    model = Book
    template_name = 'books1.html'
    context_object_name = 'books_list'


class BooksDemo2(ListView):
    model = Book
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_list'] = Book.objects.all()
        return context


class BooksDemo5(ListView):
    model = Book
    template_name = 'books1.html'
    context_object_name = 'books_list'
    queryset = Book.objects.filter(name__istartswith='M')


class BooksDemo3(DetailView):
    model = Book
    template_name = 'books2.html'
    context_object_name = 'books_list'


class BooksDemo4(DetailView):
    model = Book
    template_name = 'books2.html'
    context_object_name = 'books_list'

    def get_queryset(self):
        # filter books with pk=1
        return Book.objects.filter(pk=self.kwargs['pk'])


class BooksDemo6(DetailView):
    model = Book
    template_name = 'books2.html'
    context_object_name = "books_list"
    queryset = Book.objects.all()

    def get_object(self):
        obj = super().get_object()
        # update the name of current book object provided in url id
        obj.name = "name updated"
        obj.save()
        return obj


class AboutPage(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello"
        return context


class TemplateDemo(TemplateView):
    def setup(self, request, *args, **kwargs):
        print("Performs key view initialization prior to dispatch().")
        self.request = request
        self.args = args
        self.kwargs = kwargs

    template_name = 'page2.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['message1'] = "Hello"
        return contex

    def post(self, request):
        if request.method == "POST":
            data = request.POST['msg']
            return render(request, self.template_name, {'msg': data})


# Class Based view using View

class ViewDemo(View):
    # to specify which methods to be allowed
    http_method_names = ['get', 'post']

    def setup(self, request, *args, **kwargs):
        print("Performs key view initialization prior to dispatch().")
        self.request = request
        self.args = args

    def dispatch(self, request, *args, **kwargs):
        print("The view part of the view – the method that accepts a request argument plus arguments, and returns an "
              "HTTP response.")
        return render(request, 'page1.html', {'msg': 'Hello'})

    def http_method_not_allowed(self, request, *args, **kwargs):
        print(request.method, "Not allowed")
        return HttpResponseNotAllowed("Methods not allowed")

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Content-Length'] = 12
        return response


class ViewDemo2(View):
    def setup(self, request, *args, **kwargs):
        print("Performs key view initialization prior to dispatch().")
        self.request = request
        self.args = args

    # this will handle get requests
    def get(self, request, *args, **kwargs):
        print("Get Method")
        return render(request, 'page1.html', {'msg': 'Hello'})

    # this will handle post request
    def post(self, request):
        message = request.POST['msg']
        return render(request, 'page1.html', {'message': message, 'msg': 'Hello'})
