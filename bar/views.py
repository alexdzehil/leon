from django.shortcuts import render

from .models import GalleryPhoto, ImageMenu, MainPageConfig, Menu, MetaInfo, Slide, SubMenu


def index(request):
    meta_info = MetaInfo.objects.get()
    config = MainPageConfig.objects.get()
    slide = Slide.objects.all()
    photos = GalleryPhoto.objects.all()

    context = {
        'meta': meta_info,
        'slide': slide,
        'photos': photos,
        'config': config
    }
    return render(request, 'index.html', context)


def menu(request):
    meta_info = MetaInfo.objects.get()
    config = MainPageConfig.objects.get()
    menu = Menu.objects.get()
    submenu = SubMenu.objects.select_related('config').all()
    image_menu = ImageMenu.objects.all()

    context = {
        'menu': menu,
        'submenu': submenu,
        'image_menu': image_menu,
        'meta': meta_info,
        'config': config
    }
    return render(request, 'menu.html', context)
