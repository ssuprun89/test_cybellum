class BaseService:
    @classmethod
    def get_service(cls, *args, **kwargs):
        return cls()
