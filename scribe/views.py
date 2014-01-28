from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from guardian.mixins import LoginRequiredMixin

from scribe.models import Template, Header, Email

# Templates
class TemplateMixin(object):
    model = Template
    def get_success_url(self):
        return reverse('template_detail', kwargs={'pk': self.object.pk})
    # def get_queryset(self):
    #     return Template.objects.filter(template__user-self.request.user)
    
class TemplateIndex(LoginRequiredMixin, TemplateMixin, ListView):
    template_name = 'template/index.html'

class TemplateDetail(LoginRequiredMixin, TemplateMixin, DetailView):
    template_name = 'template/detail.html'

class TemplateCreate(LoginRequiredMixin, TemplateMixin, CreateView):
    template_name = 'create.html'

class TemplateUpdate(LoginRequiredMixin, TemplateMixin, UpdateView):
    template_name = 'update.html'

class TemplateDelete(LoginRequiredMixin, TemplateMixin, DeleteView):
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('template_index')

# Header
class HeaderMixin(object):
    model = Header
    def get_success_url(self):
        return reverse('header_detail', kwargs={'pk': self.object.pk})

class HeaderIndex(LoginRequiredMixin, HeaderMixin, ListView):
    header_name = 'header/index.html'

class HeaderDetail(LoginRequiredMixin, HeaderMixin, DetailView):
    header_name = 'header/detail.html'

class HeaderCreate(LoginRequiredMixin, HeaderMixin, CreateView):
    header_name = 'create.html'

class HeaderUpdate(LoginRequiredMixin, HeaderMixin, UpdateView):
    header_name = 'update.html'

class HeaderDelete(LoginRequiredMixin, HeaderMixin, DeleteView):
    header_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('header_index')

# Email
class EmailMixin(object):
    model = Email
    def get_success_url(self):
        return reverse('scribe:email:email_detail', kwargs={'pk': self.object.pk})

class EmailIndex(LoginRequiredMixin, EmailMixin, ListView):
    template_name = 'email/index.html'

class EmailDetail(LoginRequiredMixin, EmailMixin, DetailView):
    template_name = 'email/detail.html'

class EmailCreate(LoginRequiredMixin, EmailMixin, CreateView):
    template_name = 'create.html'

class EmailUpdate(LoginRequiredMixin, EmailMixin, UpdateView):
    template_name = 'update.html'

class EmailDelete(LoginRequiredMixin, EmailMixin, DeleteView):
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('email_index')
