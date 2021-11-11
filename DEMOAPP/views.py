from django.shortcuts import HttpResponse , render




# Create your views here.

def index(request):
    #return HttpResponse("THIS IS MY WEBSITE ") 
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html' )
def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return  render(request, 'projects.html')
