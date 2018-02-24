from django.views.generic import TemplateView
from IDaaS.models import LdapUser

class LoginView(TemplateView):
    template_name = "login.html"


class ProfileView(TemplateView):
    template_name = "profile.html"

    # first check if user has ldap account
    # yes - show change pwd form
    # no - write error msg
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            LdapUser.objects.get(email=self.request.user)
            context['hasLdap'] = True
        except LdapUser.DoesNotExist:
            context['hasLdap'] = False
        
        context['user'] = self.request.user
        return context

