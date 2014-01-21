from django.shortcuts import render

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
