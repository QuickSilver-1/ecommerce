from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer


menu = [
        ['О сайте', 'Покупателям', 'Юридическим лицам'], 

        [['О компании', 'Новости', 'Партнерам','Вакансии','Политика конфиденциальности','Персональные данные','Правила продаж','Правила пользования сайта'],
         ['Как формить заказ','Способы оплаты','Кредиты','Доставка','Статус заказа','Обмен, возврат, гарантия','Юридическим лицам','Помощь'],
         ['+79228884485 (с 8:00 до 22:00)', 'prusakov_2005@mail.ru']]
       
       ]

def index(request):
    return render(request, 'musicforce/index.html', {'name':Customer.objects.get(id=1).first_name, 'menu':menu})

def categories(request):
    return render(request, 'musicforce/categories.html', {'menu':menu})

def red(request):
    return redirect('xui', permanent=True)

def go_on_hui(request):
    return HttpResponse('Иди нахуй!')

def pageNotFound(request, exception):
    return HttpResponse('Page not Found')
