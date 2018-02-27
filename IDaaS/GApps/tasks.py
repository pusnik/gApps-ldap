import secrets
import requests
import string

from django.contrib.auth.models import User

from IDaaS.models import LdapUser
from IDaaS.models import LdapGroup

ALPHABET = string.ascii_letters + string.digits

def copyToLdap(user_email):
    """
    Task to copy GApps users to LDAP directory
    """
    user = User.objects.get(email=user_email)
    social = user.social_auth.get(provider='google-oauth2')
    print ("Get social")
    print (social)
    domain = user_email.split('@')[1]
    print(domain)
    response = requests.get(
            'https://www.googleapis.com/admin/directory/v1/users?domain={}'.format(domain),
                params={'access_token': social.extra_data['access_token']}
        )
    print (response.json())
    gappsUsers = response.json().get('users')
    # update records
    confirmedLdapUsers = []
    for gUser in gappsUsers:
        print (gUser.get('primaryEmail'))
        try:
            usr = LdapUser.objects.get(email=gUser.get('primaryEmail'))
            #check if user needs to be deleted
            if gUser['suspended']:
                usr.delete()
                continue
        except LdapUser.DoesNotExist:
            if gUser['suspended']:
                continue
            usr = LdapUser(email=gUser.get('primaryEmail'), password = ''.join(secrets.choice(ALPHABET) for i in range(10)))
        
        usr.group = 1
        usr.uid = gUser['id'] 
        usr.first_name = gUser['name']['givenName']
        usr.last_name = gUser['name']['familyName']
        usr.full_name = gUser['name']['fullName']
        usr.username = gUser.get('primaryEmail')
        usr.home_directory = "/"
        usr.save()

        confirmedLdapUsers.append(usr.email)

    #delete users from ldap that are not gApps users
    LdapUser.objects.all().exclude(email__in=confirmedLdapUsers).delete()

    return domain