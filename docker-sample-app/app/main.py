import falcon


class RootDocumentHandler:

    def on_get(self, req, res):
        res.status = '200'
        res.content_type = 'text/html'
        res.body = '<h1>Hello Tech Summit</h1>'


app = falcon.API()
app.add_route('/', RootDocumentHandler())