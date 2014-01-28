from django import forms
from django.conf import settings

class EmailForm(forms.Form):
    email = forms.EmailField(label=(u'Email Address'))
