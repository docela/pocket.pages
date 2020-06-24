from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'shelf/books.html')


def book(request):
    return render(request, 'shelf/book.html')


def search(request):
    return render(request, 'shelf/search.html')


def add(request):
    return render(request, 'shelf/add.html')


def statistics(request):
    return render(request, 'shelf/statistics.html')
