from app.clients import database_client
from flask import abort


class BaseManager:
    def __init__(self, model):
        self.model = model
        self._client = database_client

    def _generate_filter_criteria(self, **kwargs):
        operations = {
            "": lambda k, v: getattr(self.model, k) == v,
            "in": lambda k, v: getattr(self.model, k).in_(v),
        }
        criteria = []
        for k, v in kwargs.items():
            check = k.split("__")
            criteria.append(
                operations[""](k, v)
                if len(check) == 1
                else operations[check[1]](check[0], v)
            )
        return criteria

    def get(self, **kwargs):
        return self._client.get(self.model, *self._generate_filter_criteria(**kwargs))

    def get_or_none(self, **kwargs):
        return self._client.get_or_none(
            self.model, *self._generate_filter_criteria(**kwargs)
        )

    def get_or_404(self, **kwargs):
        obj = self._client.get_or_none(
            self.model, *self._generate_filter_criteria(**kwargs)
        )
        if obj:
            return obj
        else:
            abort(404, "Object not found")

    def count(self, **kwargs):
        return self._client.count(self.model, *self._generate_filter_criteria(**kwargs))

    def filter(self, **kwargs):
        return self._client.filter(
            self.model, *self._generate_filter_criteria(**kwargs)
        )

    def update(self, defaults, **kwargs):
        return self._client.update(
            self.model,
            defaults=defaults,
            criterion=self._generate_filter_criteria(**kwargs),
            refresh=True,
        )

    def create(self, **kwargs):
        generate_save_data = {k: v for k, v in kwargs.items() if "__" not in k}
        return self._client.create(self.model, **generate_save_data)

    def get_or_create(self, defaults: dict, **kwargs):
        obj = self.get_or_none(**kwargs)
        if obj:
            return obj, False
        defaults.update(kwargs)
        new_data = defaults
        return self.create(**new_data), True

    def update_or_create(self, defaults, **kwargs):
        obj = self.get_or_none(**kwargs)
        if obj:
            return self.update(defaults, **kwargs), False
        else:
            defaults.update(kwargs)
            new_data = defaults
            return self.create(**new_data), True
