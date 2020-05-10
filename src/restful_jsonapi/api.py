import json
from functools import partial

from restful_jsonapi.serializer import Serializer


class API:

    def __init__(self, session):
        self.prefix = '/api'
        self.session = session

        self._collection_name_to_model = dict()
        self._serializers = dict()

    def dispatch_request(self, method, *args, **kwargs):
        content = method(*args, **kwargs)
        json_content = json.dumps(content)
        return self.create_response(content=json_content)

    def create_response(self, content):
        raise NotImplemented

    def get_resource(self, resource_type, resource_id):
        model = self._collection_name_to_model[resource_type]
        instance = self.session.query(model).get(resource_id)
        data = {
            'type': resource_type,
            'id': resource_id,
            'attributes': self._serializers[model].get_attributes(instance)
        }

        return {'data': data}

    def create_api(self, model, collection_name):
        self._collection_name_to_model[collection_name] = model
        self._serializers[model] = Serializer(model)

        resource_view_func = partial(self.dispatch_request, self.get_resource, collection_name)
        self.add_route(f'{self.prefix}/{collection_name}/<resource_id>', methods=['GET'], view_function=resource_view_func)

    def add_route(self, path, methods, view_function):
        raise NotImplemented
