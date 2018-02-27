import requests

def get_avatar(request, backend, strategy, details, response,
        user=None, *args, **kwargs):
    """
    Get user avatar image and verify if admin. Save data to request session.
    """
    url = None
    if backend.name == 'google-oauth2':
        print(response)
        url = response['image'].get('url')
        ext = url.split('.')[-1]
        domain = response['domain']
        user_id = response['id']
    if url:
        request.session['avatar_url'] = url.split('?')[0]+'?sz=200'
    if domain and user_id:
        #check if user is admin
        social = user.social_auth.get(provider='google-oauth2')       
        response = requests.get(
            ' https://www.googleapis.com/admin/directory/v1/users/{}'.format(user_id),
                params={'access_token': social.extra_data['access_token']}
        )
        print ("User data")
        print (response.json())
        request.session['isAdmin'] = response.json().get('isAdmin')
        request.session['domain'] = domain


