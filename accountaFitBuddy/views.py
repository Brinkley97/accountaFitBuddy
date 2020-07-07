# importing the HttpResponse module; when the user request a page, this will allow me to send something back
from django.http import HttpResponse
from django.shortcuts import render

# homepage function a request parameter/ object
def homepage(request):
    return render(request, "index.html")
# about function a request parameter/ object
def about(request):
    return render(request, "about.html")

def myPage(request):
    return render(request, "myPage.html")
