from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseForbidden
from django.utils.html import escapejs
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from guardian.shortcuts import assign_perm, get_objects_for_user
from guardian.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from thoth.settings import WEB_URL
from guardian.models import Group

from scribe.models import Template, Header, Email
from scribe.forms import UploadImage

# Permission
def write_permissions(self):
    permission_list = ['add_email', 'change_email', 'delete_email', 'view_email'];
    for group in Group.objects.all():
        for permission in permission_list:
            if group.permissions.filter(codename=permission):
                assign_perm(permission, group, self.object)
    for permission in permission_list:
        assign_perm(permission, self.request.user, self.object)

def upload(request):
    if request.method == 'POST':
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>" % ('http://' + WEB_URL + image.get_absolute_url()))
        print('invalid')
        return HttpResponse("<script>alert('%s');</script>" % escapejs('\n'.join([v[0] for k, v in form.errors.items()])))
    return HttpResponseForbidden('Allowed only via POST')

# Email
class EmailMixin(object):
    model = Email
    def get_success_url(self):
        return reverse('scribe:email:email_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        qs = Email.objects.all()
        return get_objects_for_user(self.request.user, 'view_email', qs)

class EmailIndex(LoginRequiredMixin, EmailMixin, ListView):
    template_name = 'scribe/email/index.html'

class EmailDetail(LoginRequiredMixin, EmailMixin, DetailView):
    template_name = 'scribe/email/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmailDetail, self).get_context_data(**kwargs)
        contents = context['object'].template.template
        contents = contents.replace("{ CONTENTS HERE }", context['object'].content)
        contents = contents.replace("{ HEADER IMAGE }", ('http://' + WEB_URL + context['object'].header.image.url))
        contents = contents.replace("{ HEADER NAME }", context['object'].header.name)
        contents = contents.replace("{ HEADER LINK }", context['object'].header.link)
        context['render'] = contents
        return context

class EmailCreate(LoginRequiredMixin, EmailMixin, CreateView):
    template_name = 'scribe/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        write_permissions(self)
        return redirect(self.object)

class EmailUpdate(LoginRequiredMixin, EmailMixin, UpdateView):
    template_name = 'scribe/update.html'

class EmailDelete(LoginRequiredMixin, EmailMixin, DeleteView):
    template_name = 'scribe/confirm_delete.html'
    def get_success_url(self):
        return reverse('index')

# Templates
class TemplateMixin(object):
    model = Template
    def get_success_url(self):
        return reverse('scribe:template:template_detail', kwargs={'pk': self.object.pk})
    
class TemplateIndex(LoginRequiredMixin, TemplateMixin, ListView):
    template_name = 'scribe/template/index.html'

class TemplateDetail(LoginRequiredMixin, TemplateMixin, DetailView):
    template_name = 'scribe/template/detail.html'

class TemplateCreate(LoginRequiredMixin, TemplateMixin, CreateView):
    template_name = 'scribe/template/create.html'

    @method_decorator(permission_required('scribe.add_template'))
    def dispatch(self, *args, **kwargs):
        return super(TemplateCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return redirect(self.object)

class TemplateUpdate(LoginRequiredMixin, TemplateMixin, UpdateView):
    template_name = 'scribe/template/update.html'

    @method_decorator(permission_required('scribe.change_template'))
    def dispatch(self, *args, **kwargs):
        return super(TemplateUpdate, self).dispatch(*args, **kwargs)

class TemplateDelete(LoginRequiredMixin, TemplateMixin, DeleteView):
    template_name = 'scribe/confirm_delete.html'

    @method_decorator(permission_required('scribe.delete_template'))
    def dispatch(self, *args, **kwargs):
        return super(TemplateDelete, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('scribe:template:template_index')

# Header
class HeaderMixin(object):
    model = Header
    def get_success_url(self):
        return reverse('scribe:header:header_detail', kwargs={'pk': self.object.pk})

class HeaderIndex(LoginRequiredMixin, HeaderMixin, ListView):
    template_name = 'scribe/header/index.html'

class HeaderDetail(LoginRequiredMixin, HeaderMixin, DetailView):
    template_name = 'scribe/header/detail.html'

class HeaderCreate(LoginRequiredMixin, HeaderMixin, CreateView):
    template_name = 'scribe/create.html'

    @method_decorator(permission_required('scribe.add_header'))
    def dispatch(self, *args, **kwargs):
        return super(HeaderCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return redirect(self.object)

class HeaderUpdate(LoginRequiredMixin, HeaderMixin, UpdateView):
    template_name = 'scribe/update.html'

    @method_decorator(permission_required('scribe.change_header'))
    def dispatch(self, *args, **kwargs):
        return super(HeaderUpdate, self).dispatch(*args, **kwargs)

class HeaderDelete(LoginRequiredMixin, HeaderMixin, DeleteView):
    template_name = 'scribe/confirm_delete.html'

    @method_decorator(permission_required('scribe.delete_header'))
    def dispatch(self, *args, **kwargs):
        return super(HeaderDelete, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('scribe:header:header_index')

