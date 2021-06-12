from django import template

register = template.Library()


@register.simple_tag
def subtract(one, two):
    return int(one) - int(two)


@register.filter
def declenize(num, nouns):
    nouns = nouns.strip().split()
    remains = int(num) % 10

    if remains == 1:
        return f'{num} {nouns[0]}'
    elif remains > 1 and remains < 5:
        return f'{num} {nouns[1]}'
    else:
        return f'{num} {nouns[2]}'
