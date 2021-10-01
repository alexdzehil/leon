from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from sorl.thumbnail import ImageField

from django.db import models


class MainPageConfig(SingletonModel):
    slide_title = models.CharField('Заголовок сайдбара',
                                   max_length=255,
                                   blank=True, null=True)
    gallery_title = models.CharField('Заголовок галлереи',
                                     max_length=50,
                                     blank=True, null=True)

    about_title = models.CharField('Заголовок о клубе',
                                   max_length=15,
                                   blank=True, null=True)
    info = models.TextField('Описание клуба',
                            blank=True, null=True)
    image = ImageField('Фото о клубе',
                       blank=True, null=True,
                       upload_to='uploaded_images')

    contacts_title = models.CharField('Заголовок контакты',
                                      max_length=15)
    phone = models.CharField('Телефон',
                             max_length=20,
                             blank=True, null=True)
    email = models.EmailField('Электронная почта',
                              max_length=200,
                              blank=True, null=True)
    schedule = models.CharField('Режим работы',
                                max_length=200,
                                blank=True, null=True)

    def __str__(self):
        return 'Конфигурация сайта'

    class Meta:
        verbose_name = 'Конфигурация сайта'
        verbose_name_plural = 'Конфигурация сайта'


class MetaInfo(SingletonModel):
    config = models.ForeignKey(MainPageConfig,
                               blank=True, null=True,
                               on_delete=models.CASCADE)
    description_search = models.CharField('Описание для поисковой выдачи',
                                          max_length=255,
                                          blank=True, null=True)
    keywords = models.CharField('Ключевые слова для поисковой выдачи',
                                max_length=255,
                                blank=True, null=True)
    format_detection = models.CharField('Формат для поисковой выдачи',
                                        max_length=255,
                                        blank=True, null=True)

    def __str__(self):
        return 'Информация для поисковых систем'

    class Meta:
        verbose_name = 'Информация для поисковых систем'
        verbose_name_plural = 'Информация для поисковых систем'


class Slide(models.Model):
    config = models.ForeignKey(MainPageConfig,
                               blank=True, null=True,
                               on_delete=models.CASCADE)
    title = models.CharField('Заголовок сайдбара',
                             max_length=255,
                             blank=True, null=True)
    description = RichTextField('Описание',
                                   blank=True, null=True)
    image = ImageField('Фото в сайдбар',
                       blank=True, null=True)

    def __str__(self):
        return 'Сайдбар'

    class Meta:
        verbose_name = 'Сайдбар'
        verbose_name_plural = 'Сайдбар'


class GalleryPhoto(models.Model):
    config = models.ForeignKey(MainPageConfig,
                               blank=True, null=True,
                               on_delete=models.CASCADE)
    image = ImageField('Галлерея',
                       blank=True,null=True)

    def __str__(self):
        return 'Фотогаллерея'

    class Meta:
        verbose_name = 'Фотогаллерея'
        verbose_name_plural = 'Фотогаллерея'


class Menu(SingletonModel):
    title = models.CharField('Заголовок меню',
                             max_length=50,
                             blank=True, null=True)

    def __str__(self):
        return 'Меню'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class SubMenu(models.Model):
    config = models.ForeignKey(Menu,
                               blank=True, null=True,
                               on_delete=models.CASCADE)
    title = models.CharField('Подзаголовок меню',
                             max_length=50,
                             blank=True, null=True)

    def __str__(self):
        return 'Подменю'

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'


class ImageMenu(models.Model):
    owner = models.ForeignKey(SubMenu,
                              blank=True, null=True,
                              on_delete=models.CASCADE,
                              related_name='images')
    image = ImageField('Фото меню',
                       blank=True, null=True)

    def __str__(self):
        return 'Фото меню'

    class Meta:
        verbose_name = 'Фото меню'
        verbose_name_plural = 'Фото меню'
