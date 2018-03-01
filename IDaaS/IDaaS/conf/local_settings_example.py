import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'ldap': {
        'ENGINE': 'ldapdb.backends.ldap',
        'NAME': 'ldap://IP',
        'USER': 'cn=admin,dc=domain,dc=com',
        'PASSWORD': 'ldapPassword',
     },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

BASE_DN_USER = "ou=people,dc=domain,dc=com"
BASE_DN_GROUP = "ou=groups,dc=domain,dc=com"

# G Oauth2 keys
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "xxxx.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "secret"
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ["https://www.googleapis.com/auth/admin.directory.user.readonly"]
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/admin.directory.group.readonly", "https://www.googleapis.com/auth/admin.directory.user"]