from django.shortcuts import redirect
from django.urls import reverse


def login_required_redirect(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('accounts:index'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view