from django.shortcuts import render

from .models import MainPageConfig, Slide, GalleryPhoto, Menu, SubMenu, ImageMenu, MetaInfo


def index(request):
    meta_info = MetaInfo.objects.select_related('config').get()
    slide = Slide.objects.all()
    photos = GalleryPhoto.objects.all()

    context = {
        'meta': meta_info,
        'slide': slide,
        'photos': photos,
    }
    return render(request, 'index.html', context)


def menu(request):
    meta_info = MetaInfo.objects.select_related('config').get()
    menu = Menu.objects.get()
    submenu = SubMenu.objects.select_related('config').all()
    image_menu = ImageMenu.objects.all()

    context = {
        'menu': menu,
        'submenu': submenu,
        'image_menu': image_menu,
        'meta': meta_info,
    }
    return render(request, 'menu.html', context)
