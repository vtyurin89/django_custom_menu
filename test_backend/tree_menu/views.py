from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tree_menu/index.html')

