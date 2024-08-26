from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200) #brand(marca)
    factory_year = models.IntegerField(blank=True,null=True) #factoryYear(AnoDefábrica)
    model_year = models.IntegerField(blank=True,null=True)
    value = models.FloatField(blank=True,null=True)

# para resolver a nomeclatura la no banco de dados e tirar o object Car

    def __str__(self):
        return self.model # ao inves de aparecer object vai aparecer o nome do carro