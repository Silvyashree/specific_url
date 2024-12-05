from django.shortcuts import render

# Create your views here.
def dairy(request):
    return render(request, 'dairy.html') 

def chocolate(request):
    return render(request, 'chocolate.html')