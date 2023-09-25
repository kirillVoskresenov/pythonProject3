from django import template

register = template.Library()

Bad_words = ("дурак","редиска")

@register.filter()
def censor(value):
    for i in Bad_words:
        value = value.replace(i,i[:1]+ '*'*(len(i)-1))
    return value