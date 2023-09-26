from django import template

register = template.Library()

bad_words = ["дурак","редиска"]

@register.filter()
def censor(value):
    for i in bad_words:
        value = value.replace(i,i[:1]+ '*'*(len(i)-1)).lower()
    return value