from django.template import Library

register = Library()

@register.filter(name='get_range')
def getRange(value):
    return range(value)

@register.filter(name='index_to_price')
def indexToPrice(value):
    return value * 10000