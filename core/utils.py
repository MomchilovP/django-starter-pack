from django.utils.translation import gettext_lazy as _

from django.conf import settings

def environment_callback(request):
    if settings.DEBUG:
        return [_("Development"), "info"]

    return [_("Production"), "warning"]