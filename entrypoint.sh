#!/bin/sh

# migrate migrations
alembic upgrade head

exec "$@"
