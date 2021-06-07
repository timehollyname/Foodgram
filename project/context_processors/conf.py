from django.conf import settings


def conf(request):
    return {'conf': settings}
