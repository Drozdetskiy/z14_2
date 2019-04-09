import traceback

from django.core.exceptions import MiddlewareNotUsed

from social_cooking import settings


def my_first_middleware(get_response):
    def _inner(request):
        print('sdf')
        response = get_response(request)
        print('post req')
        return response
    return _inner


class MySecondMiddleware:
    def __init__(self, get_response):
        if not settings.DEBUG:
            raise MiddlewareNotUsed
        self.get_response = get_response

    def __call__(self, request):
        print('sdfsfd')
        response = self.get_response(request)
        print('dsfsdffsd', response.status_code)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('por', view_func, view_args, view_kwargs)

    def process_exeption(self, request, exception):
        print('process_exceprion', exception, traceback.fomate_exc())

    def process_template_response(self, requets, response):
        print('process template')
        return response
