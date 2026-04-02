from django.http import HttpResponse

def homepage(request):
    return HttpResponse("my first app in django")

def About(request):
    return HttpResponse("This is my About us page")