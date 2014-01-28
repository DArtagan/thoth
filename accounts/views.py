from django.views.generic.edit import FormView
from guardian.mixins import LoginRequiredMixin

from accounts.models import User
from accounts.forms import EmailForm

class EmailUpdate(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_email.html'
    form_class = EmailForm
    model = User
    success_url = '/'

    def form_valid(self, form):
        self.request.user.email = form.cleaned_data.get('email')
        self.request.user.save(update_fields=['email'])
        return super(EmailUpdate, self).form_valid(form)
