from django import template

register = template.Library()


@register.simple_tag
def get_global_counter(inner, outer, items):
    print(inner)
    print(outer)
    print(items)
    print('='*80)
    return int(inner)
