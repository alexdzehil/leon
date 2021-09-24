from django.db import models

from solo.models import SingletonModel
from sorl.thumbnail import ImageField


class MainPageConfig(SingletonModel):
    slide_title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Заголовок сайдбара')
    gallery_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Заголовок галлереи')

    about_title = models.CharField(max_length=15, null=True, blank=True, verbose_name='Заголовок о клубе')
    info = models.TextField(null=True, blank=True, verbose_name='Описание клуба')
    image = ImageField(null=True, blank=True, upload_to='uploaded_images', verbose_name='Фото о клубе')

    contacts_title = models.CharField(max_length=15, verbose_name='Заголовок контакты')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Электронная почта')
    schedule = models.CharField(max_length=200, null=True, blank=True, verbose_name='Режим работы')

    def __str__(self):
        return 'Конфигурация сайта'

    class Meta:
        verbose_name = 'Конфигурация сайта'
        verbose_name_plural = 'Конфигурация сайта'


class MetaInfo(SingletonModel):
    config = models.ForeignKey(MainPageConfig, null=True, blank=True, on_delete=models.CASCADE)
    description_search = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание для поисковой выдачи')
    keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ключевые слова для поисковой выдачи')
    format_detection = models.CharField(max_length=255, null=True, blank=True, verbose_name='Формат для поисковой выдачи')

    def __str__(self):
        return 'Информация для поисковых систем'

    class Meta:
        verbose_name = 'Информация для поисковых систем'
        verbose_name_plural = 'Информация для поисковых систем'


class Slide(models.Model):
    config = models.ForeignKey(MainPageConfig, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Заголовок сайдбара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = ImageField(null=True, blank=True, verbose_name='Фото в сайдбар')

    def __str__(self):
        return 'Сайдбар'

    class Meta:
        verbose_name = 'Сайдбар'
        verbose_name_plural = 'Сайдбар'


class GalleryPhoto(models.Model):
    config = models.ForeignKey(MainPageConfig, null=True, blank=True, on_delete=models.CASCADE)
    image = ImageField(null=True, blank=True, verbose_name='Галлерея')

    def __str__(self):
        return 'Фотогаллерея'

    class Meta:
        verbose_name = 'Фотогаллерея'
        verbose_name_plural = 'Фотогаллерея'


class Menu(SingletonModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Заголовок меню')

    def __str__(self):
        return 'Меню'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class SubMenu(models.Model):
    config = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Подзаголовок меню')

    def __str__(self):
        return 'Подменю'

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'


class ImageMenu(models.Model):
    owner = models.ForeignKey(SubMenu, null=True, blank=True, on_delete=models.CASCADE, related_name='images')
    image = ImageField(null=True, blank=True, verbose_name='Фото меню')

    def __str__(self):
        return 'Фото меню'

    class Meta:
        verbose_name = 'Фото меню'
        verbose_name_plural = 'Фото меню'
