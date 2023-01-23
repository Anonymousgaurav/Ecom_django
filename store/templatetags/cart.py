from django import template

register = template.Library()


# function to get either product is available or not in our cart
@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False
