from django.shortcuts import render
from cars.models import Car
# from django.http import HttpResponse

# Create your views here.
# def cars_view(request):
#     return HttpResponse()

def cars_view(request):
    # cars = Car.objects.all()#(select * from Car) busque todos objeto de Car(atraves o ORM do Django)
    #print(cars) # mostrar no terminal
    # cars = Car.objects.filter(brand__name='Fiat') # pq estou navegando de tabela p tabela pois 
    #brand e uma chave estranjeira
    # cars = Car.objects.filter(brand=1) # filtar todos carros da marca fiat o id é 1
    # cars = Car.objects.filter(model='Chevette tubarão') # ele traz com nome especifico
    # cars = Car.objects.filter(model__contains='c') # basta um dos nomes ele ja busca
    # print(request) # ele uso metodo GET p buscar
    # print(request.GET)
    # print(request.GET.get('search')) #
    cars = Car.objects.all().order_by('model') # traz todos
    # cars = Car.objects.all().order_by('-model') # - inverte a ordem
    search = request.GET.get('search') # search busca q user faz
    if search:
        # cars = cars.filter(model__contains=search).order_by('model')
        cars = cars.filter(model__contains=search) # ñ precisa colocra novamente
        # cars = Car.objects.filter(model__contains=search) # filtra o q contem o q user digitar
    return render(
        request, 
        'cars.html', 
        # {'cars':{'model':'Celta 1.0'}}
        {'cars': cars }
    ) #cars.html esta na pasta de templates
