from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def cars_view(request):
#     return HttpResponse()

def cars_view(request):
    return render(request, 'cars.html') #cars.html esta na pasta de templates
