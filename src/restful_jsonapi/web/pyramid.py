from pyramid.response import Response

from restful_jsonapi.api import API
from restful_jsonapi.constants import CONTENT_TYPE


class PyramidAPI(API):

    def __init__(self, *args, config=None):
        super().__init__(*args)
        self.config = config

    def add_route(self, path, methods, view_function):

        def view(request):
            resource_id = request.matchdict['resource_id']
            return Response(view_function(resource_id), content_type=CONTENT_TYPE, charset='utf-8')

        self.config.add_route('index', '/{resource_id}')
        self.config.add_view(view, route_name='index')
        # self.config.add_url_rule(path, endpoint='pass', methods=methods, view_func=view_function)

    def create_response(self, content):
        # response = Response(content)
        # # response.headers['Content-Type'] = CONTENT_TYPE
        return content
