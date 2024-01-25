from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request):
    my_str_1 = "Мы первая компания которая купит у вас все и да-же немного больше"
    my_str_2 = "Наши довольные клиенты"
    my_str_3 = "Клиент1:"
    my_str_4 = "Инфо о клиенте"
    my_str_5 = "Клиент2:"
    my_str_6 = "Инфо о клиенте"
    return render(request, 'index.html', {
        'my_str_1': my_str_1,
        'my_str_2': my_str_2,
        'my_str_3': my_str_3,
        'my_str_4': my_str_4,
        'my_str_5': my_str_5,
        'my_str_6': my_str_6
    })


def aboutus(request):
    my_str_1 = "Возможно вы хотите узнать больше о нас?"
    my_str_2 = "Адрес:город Москва, улица Пушкина д 92."
    my_str_3 = 'Полное название:Общество с ограниченной ответственностью "Покупаем продаем"'
    my_str_4 = "Наш директор:"
    return render(request, 'aboutus.html', {
        'my_str_1': my_str_1,
        'my_str_2': my_str_2,
        'my_str_3': my_str_3,
        'my_str_4': my_str_4
    })
