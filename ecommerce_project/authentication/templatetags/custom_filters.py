from django import template
from user_cart.models import CartItem

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

@register.filter
def get_cart_item(product, user):
    try:
        return CartItem.objects.get(product=product, user=user)
    except CartItem.DoesNotExist:
        return None
    
@register.filter
def multiply(value, arg):
    return value * arg
