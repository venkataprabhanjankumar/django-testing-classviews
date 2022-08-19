# https://docs.djangoproject.com/en/4.1/topics/http/middleware/
class AuthMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # in middleware call method is executed for every request
        # We can make a Middlewares that just overrides the __call__() method
        # put Code here to be executed for each request before
        # the view (and later middleware) are called.
        print(request.user)
        print("Executes for each request before thw view start executed")
        response = self.get_response(request)
        # put Code here to be executed for each request/response after
        # the view is called.
        print("Executes After view is called for every request")
        return response
