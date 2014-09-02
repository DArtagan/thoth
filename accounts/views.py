from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from guardian.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import PasswordResetForm
from authtools.views import PasswordResetView
from accounts.forms import UserCreationForm
from guardian.models import Group
from thoth.settings import WEB_URL

from accounts.models import User
from accounts.forms import ProfileForm

class Users(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/users.html'

    def get_queryset(self):
        return User.objects.all().order_by('name')

    @method_decorator(permission_required('accounts.edit_user'))
    def dispacth(self, *args, **kwargs):
        return super(Users, self).dispatch(*args, **kwargs)

class AddUser(LoginRequiredMixin, FormView):
    form_class = UserCreationForm
    model = User
    template_name = 'accounts/add_user.html'
    success_url = '/accounts/users/'

    @method_decorator(permission_required('accounts.add_user'))
    def dispacth(self, *args, **kwargs):
        return super(AddUser, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if not form.data['password1']:
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            form.instance.set_password(get_random_string())
            reset_password = True
        else:
            reset_password = False

        form.save()

        if reset_password:
            print(form.data['email'])
            reset_form = PasswordResetForm({'email': form.data['email']})
            assert reset_form.is_valid()
            reset_form.save(
                subject_template_name='registration/account_creation_subject.txt',
                email_template_name='registration/account_creation_email.html',
                domain_override=WEB_URL,
            )
            reset_form = PasswordResetView
        return super(AddUser, self).form_valid(form)

class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/confirm_delete.html'
    success_url = '/accounts/users/'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/update_profile.html'
    form_class = ProfileForm
    model = User
    success_url = '/'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)

@login_required
def promote(request, pk):
    user = User.objects.get(pk=pk)
    g = Group.objects.get(name='csmaa')
    g.user_set.add(user)
    return HttpResponseRedirect(reverse('accounts:users'))

@login_required
def demote(request, pk):
    user = User.objects.get(pk=pk)
    g = Group.objects.get(name='csmaa')
    g.user_set.remove(user)
    return HttpResponseRedirect(reverse('accounts:users'))
