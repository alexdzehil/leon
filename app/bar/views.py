from django.shortcuts import render

from .models import MainPageConfig, Slide, GalleryPhoto, Menu, SubMenu, ImageMenu


def index(request):
    config = MainPageConfig.objects.get()
    slide = Slide.objects.all()
    photos = GalleryPhoto.objects.all()

    context = {
        'config': config,
        'slide': slide,
        'photos': photos,
    }
    return render(request, 'index.html', context)


def menu(request):
    config = MainPageConfig.objects.get()
    menu = Menu.objects.get()
    submenu = SubMenu.objects.all()
    image_menu = ImageMenu.objects.all()

    context = {
        'menu': menu,
        'submenu': submenu,
        'image_menu': image_menu,
        'config': config
    }
    return render(request, 'menu.html', context)
