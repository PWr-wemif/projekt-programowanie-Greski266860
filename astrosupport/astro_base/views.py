from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the astro_base index.")