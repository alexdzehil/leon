from django.contrib import admin

from solo.admin import SingletonModelAdmin
import nested_admin

from .models import MainPageConfig, Slide, GalleryPhoto, Menu, SubMenu, ImageMenu


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 0


class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 0


@admin.register(MainPageConfig)
class MainPageConfigAdmin(SingletonModelAdmin):
    fields = [
        'description_search',
        'keywords',
        'format_detection',
        'gallery_title',
        'about_title',
        'info',
        'image',
        'contacts_title',
        'phone',
        'email',
        'schedule'
    ]
    inlines = [
        SlideInline,
        GalleryPhotoInline,
    ]


class ImageMenuInline(nested_admin.NestedStackedInline):
    model = ImageMenu
    extra = 0


class SubMenuInline(nested_admin.NestedStackedInline):
    model = SubMenu
    extra = 0
    inlines = [ImageMenuInline]


@admin.register(Menu)
class MenuAdmin(SingletonModelAdmin, nested_admin.NestedModelAdmin):
    inlines = [SubMenuInline]


admin.site.site_header = 'Админ-панель сайта'
