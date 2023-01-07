from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_vacancy'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    vacancies = Vacancy.objects.all()

    context = {
        'vacancies': vacancies,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'vacancy/index.html', context=context)


def about(request):
    return render(request, 'vacancy/about.html', {'menu': menu, 'title': 'О сайте'})


def addvacancy(request):
    if request.method == 'POST':
        form = AddVacancyForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddVacancyForm()
    return render(request, 'vacancy/addvacancy.html', {'form': form, 'menu': menu, 'title': 'Добавление вакансии'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_vacancy(request, vacancy_slug):
    vacancy = get_object_or_404(Vacancy, slug=vacancy_slug)

    context = {
        'vacancy': vacancy,
        'menu': menu,
        'title': vacancy.title,
        'cat_selected': vacancy.cat_id,
    }

    return render(request, 'vacancy/vacancy.html', context=context)


def show_category(request, cat_id):
    vacancies = Vacancy.objects.filter(cat_id=cat_id)

    if len(vacancies) == 0:
        raise Http404()

    context = {
        'vacancies': vacancies,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }
    return render(request, 'vacancy/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
