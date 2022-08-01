
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from demo.serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

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



class  BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)




