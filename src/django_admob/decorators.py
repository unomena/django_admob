try:
    from functools import update_wrapper
except ImportError:
    from django.utils.functional import update_wrapper  # Python 2.3, 2.4 fallback.

import admob


def analytics(view, **admob_kwargs):
    """
    Construct an AdMob analytics request.
    Requires admob.middleware.AdMobMiddleware.
    
    """
    def _dec(request, *args, **kwargs):
        admob.analytics(request, **admob_kwargs)
        request.has_admob = True
        return view(request, *args, **kwargs)
    return _dec
