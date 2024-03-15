from app.config import get_settings

settings = get_settings()


def generate_postgres_url(
    postgres_username, postgres_password, postgres_host, postgres_port, postgres_db_name
):
    return f"postgresql://{postgres_username}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db_name}"


SQLALCHEMY_DATABASE_URL = generate_postgres_url(
    settings.POSTGRES_USER,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_HOST,
    settings.POSTGRES_PORT,
    settings.POSTGRES_DB,
)
