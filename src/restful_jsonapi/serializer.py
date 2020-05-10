from sqlalchemy import inspect


class Serializer:

    def __init__(self, model):
        inspected_model = inspect(model)
        attributes = set(inspected_model.column_attrs.keys())
        attributes.remove('id')
        self._attributes = frozenset(attributes)

    def get_attributes(self, instance):
        return {attribute: getattr(instance, attribute) for attribute in self._attributes}
