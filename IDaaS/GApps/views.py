from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect

from IDaaS.models import LdapUser
from GApps.models import ScheduledSyncs
from GApps.tasks import copyToLdap

class LoginView(TemplateView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if request.user.is_authenticated == True:
            return redirect('profile')

        return super(LoginView, self).dispatch(request, *args, **kwargs)


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

def triggerSync(request):
    print("Start google sync!")
    domain = copyToLdap(request.user.email)
    obj, created = ScheduledSyncs.objects.get_or_create(user=request.user, domain=domain)
    return HttpResponse("Done")