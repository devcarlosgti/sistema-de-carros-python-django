from django.db import models

# Create your models here.

class Brand(models.Model): #tabelas marcas
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    # brand = models.CharField(max_length=200) #brand(marca)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    #fazer associação com a tabela brand(marca)
    #OndeleteModels.PROTECT -> p assegurar o user ñ delete as marcas! pois esta relacionada c carros
    factory_year = models.IntegerField(blank=True,null=True) #factoryYear(AnoDefábrica)
    model_year = models.IntegerField(blank=True,null=True)
    value = models.FloatField(blank=True,null=True)

# para resolver a nomeclatura la no banco de dados e tirar o object Car

    def __str__(self):
        return self.model # ao inves de aparecer object vai aparecer o nome do carro