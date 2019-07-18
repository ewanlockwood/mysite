from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World')

def get_index_page(request):
    return render(request, 'index.html')

def get_new_page(request):
    return render(request, 'copy.html')
