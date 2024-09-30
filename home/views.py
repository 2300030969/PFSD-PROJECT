from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')
    # return HttpResponse("this is homepage")
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
