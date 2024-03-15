class BaseClient:
    @classmethod
    def get_client(cls, *args, **kwargs):
        return cls()
