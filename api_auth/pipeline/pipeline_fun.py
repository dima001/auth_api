import hashlib


def save_profile(strategy, backend, details, response, user=None, *args, **kwargs):
    if backend.name == 'google-oauth2':
        m_token = hashlib.md5()
        m_token.update(str(response.get('access_token')))
        user.token = m_token.hexdigest()
        user.is_new = kwargs['is_new']
        user.save()