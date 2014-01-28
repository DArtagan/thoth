from django.views.generic import TemplateView
from guardian.mixins import LoginRequiredMixin

from scribe.models import Email, Template, Header

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['emails'] = Email.objects.all()
        context['templates'] = Template.objects.all()
        context['headers'] = Header.objects.all()
        return context    
