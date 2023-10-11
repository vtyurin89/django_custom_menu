from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tree_menu/index.html')


def contacts(request):
    return render(request, 'tree_menu/index.html')


def about(request):
    return render(request, 'tree_menu/index.html')


def produce(request):
    return render(request, 'tree_menu/index.html')
