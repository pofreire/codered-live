from django.shortcuts import render
from django.conf import settings

def home(request):
    url = settings.BASE_URL
    context = {
        url : 'url'
    }
    return render(request, 'home_page.html',context)
