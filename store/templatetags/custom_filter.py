from django import template

register = template.Library()


# function to get either product is available or not in our cart
@register.filter(name='currency')
def currency(number):
    return "₹ " + str(number)


