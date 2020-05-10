from restful_jsonapi.api import API
from restful_jsonapi.constants import CONTENT_TYPE


class FlaskApi(API):

    def __init__(self, *args, app=None):
        super().__init__(*args)
        self.app = app

    def add_route(self, path, methods, view_function):
        self.app.add_url_rule(path, endpoint='pass', methods=methods, view_func=view_function)

    def create_response(self, content):
        response = self.app.make_response(content)
        response.headers['Content-Type'] = CONTENT_TYPE
        return response
