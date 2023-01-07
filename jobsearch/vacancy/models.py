from django.db import models
from django.urls import reverse


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фотография')
    work_experience = models.TextField(blank=True, verbose_name='Опыт работы')
    employer = models.TextField(blank=True, verbose_name='Работодатель')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'vacancy_slug': self.slug})

    class Meta:
        verbose_name = 'вакансию'
        verbose_name_plural = 'Вакансии'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']