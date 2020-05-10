from bottle import response

from restful_jsonapi.api import API
from restful_jsonapi.constants import CONTENT_TYPE


class BottleApi(API):
    def __init__(self, *args, app=None):
        super().__init__(*args)
        self.app = app

    def add_route(self, path, methods, view_function):
        self.app.route(path, method=methods, callback=view_function)

    def create_response(self, content):
        response.content_type = CONTENT_TYPE
        return content
