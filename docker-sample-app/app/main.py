import falcon


class HelloWorldResource:

    def on_get(self, request, response):
        response.media = 'Hello Tech Summit!'


app = falcon.API()
app.add_route('/', HelloWorldResource())