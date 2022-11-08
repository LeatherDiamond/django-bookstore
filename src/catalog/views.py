from django.shortcuts import render
from django.views import generic, View
from product_card.models import Book
from django.core.paginator import Paginator
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render
from .models import Comment
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


class CatalogView(View):

    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        paginator = Paginator(book, 12)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'catalog/catalog.html',
            context={
                'page_obj': page_obj
            }
        )


class BookDetail(generic.DetailView):
    # template_name = 'catalog/book_detail.html'
    # model = Book
    # comment_form = CommentForm(request.POST)

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book)
        last_posts = Book.objects.all().order_by('-id')[:3]
        comment_form = CommentForm()
        return render(request, 'catalog/book_detail.html', context={
            'book': book,
            'last_posts': last_posts,
            'comment_form': comment_form,
        })    

    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            book = get_object_or_404(Book)
            comment = Comment.objects.create(book=book, username=username,
                                             text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'catalog/book_detail.html', context={
            'comment_form': comment_form
        })

    