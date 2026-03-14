from django.shortcuts import render

# Create your views here.
def fz(request):
    return render(request, 'fzmovies.html')

def wonder(request):
    return render(request, 'wonder.html')