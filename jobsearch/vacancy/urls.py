from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', VacancyHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addvacancy/', AddPage.as_view(), name='add_vacancy'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('vacancy/<slug:vacancy_slug>/', ShowVacancy.as_view(), name='vacancy'),
    path('category/<slug:cat_slug>/', VacancyCategory.as_view(), name='category')
]