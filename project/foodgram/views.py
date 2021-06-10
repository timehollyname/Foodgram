from django.shortcuts import render


def page_not_found(request, exception):
    context = {'path': request.path}
    return render(request, 'errors/404.html', context, status=404)


def server_error(request):
    return render(request, 'errors/500.html', status=500)


def page_bad_request(request, exception):
    return render(request, 'errors/400.html', status=400)
