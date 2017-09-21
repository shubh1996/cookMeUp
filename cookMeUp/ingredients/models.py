from django.db import models

# Create your models here.


Choices = (('veg','Vegetable'),('fruit','Fruit'),)

class maj_ingredients(models.Model):
    type_of_ingredient = models.CharField(max_length=50 , choices = Choices, default = 'Vegetable' )
    name_of_ingredient = models.CharField(max_length = 30,primary_key= True)
    def __str__(self):
        return '%s %s'%(self.name_of_ingredient)

class com_ingredients(models.Model):
    name_of_ingredient= models.CharField(max_length=50 ,primary_key= True)
    def __str__(self):
        return '%s'%(self.name_of_ingredient)

class dish(models.Model):
    name_of_dish = models.CharField(max_length = 50, primary_key = True)
    ingredient1 = models.ManyToManyField(maj_ingredients)
    ingredient2 = models.ManyToManyField(com_ingredients)
    procedure = models.TextField()
    def __str__(self):
        return '%s'%(self.name_of_dish)
    