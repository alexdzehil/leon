from django import template

from bar.models import ImageMenu, SubMenu

register = template.Library()

i = 0

@register.simple_tag
def get_global_counter(inner, outer, items, im_cou):
    count = ImageMenu.objects.all().count()
    # print('Всего фото', count)
    # print('Фото в подменю', im_cou)
    # print('Итерация внутреннего цикла', inner)
    # print('Итерация внешнего цикла', outer)
    # print(items)
    # print('Искомый айдишник', count - (inner + outer))
    global i
    if i <= count:
        i += 1
        print('Искомое число', i)
    else:
        print('Все')
    print('='*80)
    return i
