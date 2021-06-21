from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        if not request.session.get('customer'):
            returnurl=request.META['PATH_INFO']
            return redirect(f'/login?return_url={returnurl}')
        response = get_response(request)
        return response
    return middleware