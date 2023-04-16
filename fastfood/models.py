from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=30, verbose_name='Email')
    password = models.CharField(max_length=35, verbose_name='Password')


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя клиента')
    card_number = models.IntegerField(verbose_name='Номер карточки')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Worker(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя работника')
    position = models.CharField(max_length=20, verbose_name='Должность')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование ингредиента')
    extra_price = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.CharField(max_length=30, verbose_name='cost calorias')



class Food(models.Model):
    name = models.CharField(max_length=255)
    start_price = models.DecimalField(max_digits=5, decimal_places=2)
    type_of_cuisine = models.CharField(max_length=30, verbose_name='Type of kitchen')
    calories = models.IntegerField(verbose_name='cost calorias')

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    vegetarian = models.BooleanField(verbose_name='vegetarians')
    food_status = models.CharField(max_length=30, verbose_name='Type of kitchen: ')
    final_price = models.IntegerField(verbose_name='Total price cost')
    order_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}, Dich: {self.food.name}, Price: {self.final_price}"
