from functools import wraps
from urllib.parse import urlparse

from django.contrib.auth.views import redirect_to_login
from django.shortcuts import resolve_url
from django.conf import settings


def check_user(function=None, login_url=None):
    def decorator(view_function):
        @wraps(view_function)
        def function_wrapper(request, *args, **kwargs):
            if str(request.user) != 'AnonymousUser':
                return view_function(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            print(resolved_login_url)
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if (not login_scheme or login_scheme == current_scheme) and (
                    not login_netloc or login_netloc == current_netloc
            ):
                path = request.get_full_path()
            print(request.path)
            return redirect_to_login(path, resolved_login_url)

        return function_wrapper

    return decorator


