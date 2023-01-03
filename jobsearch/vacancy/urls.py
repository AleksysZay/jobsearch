from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addvacancy/', addvacancy, name='add_vacancy'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('vacancy/<int:vacancy_id>/', show_vacancy, name='vacancy'),
    path('category/<int:cat_id>/', show_category, name='category')
]