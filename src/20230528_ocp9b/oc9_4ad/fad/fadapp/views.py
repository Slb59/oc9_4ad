from django.shortcuts import render


def home(request):
    return render(request, 'fadapp/home.html')
