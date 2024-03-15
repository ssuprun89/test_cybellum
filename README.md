# test_cybellum Python Flask

## Environment

For local dev and docker you need to create a `.env` file at project root containing values for the keys found in [the example env file](env.example).
A completed .env file to be used can be found in 1Password.

## Getting started

`sudo docker compose build`: creates the docker image and installs all python package dependencies for your development environment.

`sudo docker compose up -d`: spin up a local development docker container that will hot reload code changes <http://localhost:5000>

## Database

PostgresSQL

It is already installed when you created your containers.

