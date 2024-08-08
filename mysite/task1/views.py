from os import name
import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer, Game      #, Registration


# Create your views here.
def index(request):
    text1 = 'Игры'
    text2 = 'Извините ваша корзина пуста'
    context = {
        'text1': text1,
        'text2': text2,
    }
    return render(request, 'third_task/platform.html', context)

def index2(request):
    # Изменяю шаблоны согласно заданию
    list_Game_title = []
    list_Game_description = []
    list_common = []
    Game_objects = Game.objects.all()
    a = Game_objects.values()
    for i in range(0, len(a)):
        b = a[i]
        list_Game_title.append(b.get('title'))
        list_Game_description.append(b.get('description'))
        d = list_Game_title[i] + ' | ' + list_Game_description[i]
        list_common.append(d)

    context = {
        'Chess': list_common[0],
        'Ciberpunk_2077': list_common[1],
        'PayDay': list_common[2],
    }
    return render(request, 'third_task/gemes.html', context)

def index3(request):
    text4 = 'Корзина'
    context = {
        'text4': text4,
    }
    return render(request, 'third_task/cart.html', context)

list_Buyer_objects = []
# из task5
def index4(request):
    # Создаю список имен из базы данных для исключения повторений при регистрации
    Buyer_objects = Buyer.objects.all()
    a = Buyer_objects.values()
    for i in range(0, len(a)):
        b = a[i]
        list_Buyer_objects.append(b.get('name'))

    info = {}
    if request.method == 'POST':
        login = request.POST.get('login')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        age = request.POST.get('age')
        # news = Buyer.objects.all()

        if password1 == password2 and int(age) >= 18 and login not in list_Buyer_objects:
            Buyer.objects.create(name=login, password=password1, age=age, balance=0)
            return HttpResponse(f"Приветствуем, {login}")
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password1 != password2:
            info['error'] = 'Пароли не совпадают'
        elif login in list_Buyer_objects:
            info['error'] = f'Пользователь с таким логином \'{login}\' уже зарегистрирован'

    return render(request, 'fifth_task/registration_page.html', context=info)
