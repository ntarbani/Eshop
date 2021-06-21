from django import template

register=template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ " + str(number) 


@register.filter(name='multiply')
def multiply(number1,number2):
    return number1*number2 


@register.filter(name='status')
def status(flag):
    if flag:
        return 'Completed'
    else:
        return 'Pending'

