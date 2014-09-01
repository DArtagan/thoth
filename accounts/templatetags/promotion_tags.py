from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def promote(value, arg):
    """
    The template tag's syntax is {% "text"|promote:user_object %}
    """
    if not arg.groups.filter(name='csmaa').exists():
        return mark_safe('<a href="{0}">{1}</a>'.format(reverse('accounts:promote', kwargs={'pk': arg.pk}), value))
    else:
        return mark_safe(value)

@register.filter()
def demote(value, arg):
    """
    The template tag's syntax is {% "text"|demote:user_object %}
    """
    if arg.groups.filter(name='csmaa').exists():
        return mark_safe('<a href="{0}">{1}</a>'.format(reverse('accounts:demote', kwargs={'pk': arg.pk}), value))
    else:
        return mark_safe(value)
