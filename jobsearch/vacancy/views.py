from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_vacancy'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    vacancies = Vacancy.objects.all()
    cats = Category.objects.all()
    context = {
        'vacancies': vacancies,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'vacancy/index.html', context=context)


def about(request):
    return render(request, 'vacancy/about.html', {'menu': menu, 'title': 'О сайте'})


def addvacancy(request):
    return HttpResponse("Добавление вакансии")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_vacancy(request, vacancy_id):
    return HttpResponse(f"Отображение статьи с id = {vacancy_id}")


def show_category(request, cat_id):
    vacancies = Vacancy.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(vacancies) == 0:
        raise Http404()

    context = {
        'vacancies': vacancies,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }
    return render(request, 'vacancy/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
