import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django_asgi_app = get_asgi_application()
from fastfood.models import Client, Worker, Food, Ingredient, Order, User


user_azat = User(email='nikname21@gmail.com', password='defender42')
user_azat.save()
client_azat = Client(name='Nursultan Berdiev ', card_number='4147565798789009', user=user_azat)
client_azat.save()

user_altynai = User(email='altywa1998@gmail.com', password='nono34')
user_altynai.save()
worker_altynai = Worker(name='Altinai Alieva', position='Cach register operetor', user=user_altynai)
worker_altynai.save()

shaverma = Food(name='Shaverma', start_price=200,type_of_cuisine="fastfood", calories=500)
shaverma.save()
gamburger = Food(name='GAmburger', start_price=180,type_of_cuisine='fastfood', calories=350)
gamburger.save()
paste = Food(name='Paste', start_price=450,type_of_cuisine='Italian food', calories=350)
gamburger.save()
boul = Food(name='Boul', start_price=600,type_of_cuisine='European food', calories=500)
gamburger.save()
sushi = Food(name='Sushi', start_price=400 ,type_of_cuisine='Janan food', calories=450)
gamburger.save()


syro = Ingredient(name='Cheese', extra_price=80, calories=150)
syro.save()
kuritsa = Ingredient(name='Chicken', extra_price=100, calories=250)
kuritsa.save()
govyadina = Ingredient(name='BEef', extra_price=120, calories=300)
govyadina.save()
fish = Ingredient(name='fish', extra_price=120, calories=270)
fish.save()
rice = Ingredient(name='Fice', extra_price=70, calories=100)
rice.save()
curd_cheese = Ingredient(name='Curd cheese', extra_price=100, calories=170)
curd_cheese.save()
chicken_eggs = Ingredient(name='Chicken eggs', extra_price=50, calories=120)
chicken_eggs.save()
salat = Ingredient(name='Salad', extra_price=50, calories=50)
salat.save()
fri = Ingredient(name='Fri', extra_price=50, calories=70)
fri.save()


shaverma.ingredients.add(govyadina, syro, salat, fri)
gamburger.ingredients.add(kuritsa, salat)
paste.ingredients.add(salat,chicken_eggs,syro,curd_cheese)

order_azat_shaurma = Order(food=shaverma, client=client_azat, worker=worker_altynai, vegetarian=False, food_status='feast', final_price=200)
order_azat_shaurma.save()

order_azat_gamburger = Order(food=gamburger,  client=client_azat, worker=worker_altynai, vegetarian=False, food_status='feast', final_price=180)
order_azat_gamburger.save()

order_azat_paste = Order(food=paste, client=client_azat, worker=worker_altynai,  vegetarian=False, food_status='launch', final_price=450)
order_azat_paste.save()

order_azat_boul = Order(food=boul, client=client_azat, worker=worker_altynai,  vegetarian=False, food_status='snacks', final_price=600)
order_azat_boul.save()

order_azat_sushi = Order(food=sushi, client=client_azat, worker=worker_altynai,  vegetarian=True, food_status='snacks', final_price=400)
order_azat_sushi.save()

order_azat_salad = Order(food=salat, client=client_azat, worker=worker_altynai,  vegetarian=True, food_status='snacks', final_price=1200)
order_azat_salad.save()



orders_snack = Order.objects.filter(food_status='snacks')
print(f'Order with "Scnacks" status {orders_snack}')


orders_launch = Order.objects.filter(food_status='launch')
print(f'Order with "Launch" status {orders_launch}')


orders_feast = Order.objects.filter(food_status='feast')
print(f'Order with "Feast" status {orders_feast}')


orders_vegetarian = Order.objects.filter(vegetarian=True)
print(f'Order with "Vegetarian" status {orders_vegetarian}')



orders_vegetarian = Order.objects.filter(vegetarian=True)
print(f'Order with "Vegetarian" status {orders_vegetarian}')



orders_price_less_than_1000 = Order.objects.filter(final_price__lt=1000)
print(f'Orders with a total cost of up to 1000 {orders_price_less_than_1000}')

orders_price_greater_than_1000 = Order.objects.filter(final_price__gt=1000)
print(f'Orders with a total value after 1000 {orders_price_greater_than_1000}')

most_expensive_order = Order.objects.order_by('-final_price').first()
print(f'The most expensive order {most_expensive_order}')

cheapest_order = Order.objects.order_by('final_price').first()
print(f'The cheapest order {cheapest_order}')