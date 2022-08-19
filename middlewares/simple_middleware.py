def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # put Code here to be executed for each request before
        # the view (and later middleware) are called.
        print(request.user)
        response = get_response(request)

        # put Code here to be executed for each request/response after
        # the view is called.
        print("View is Executed")
        return response

    return middleware
