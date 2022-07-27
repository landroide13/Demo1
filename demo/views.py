
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.

class Index(View):

    books = Book.objects.all()
    output = ""

    for book in books:
        output += f"We have {book.title} in DB - ID {book.id} <br> "



    def get(self, request):
        return HttpResponse(self.output)


def home(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})
