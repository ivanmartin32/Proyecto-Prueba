from django.shortcuts import render


def index(request):
    return render(request, 'producto/index.html')
# Create your views here.
