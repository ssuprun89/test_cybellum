# test_cybellum Python Flask

## Environment

For local dev and docker you need to create a `.env` file at project root containing values for the keys found in [the example env file](env.example).
A completed .env file to be used can be found in 1Password.

## Getting started

`sudo bash start.sh`: creates the docker image, network, volume. And run

## Database

PostgresSQL

It is already installed when you created your containers.

## API DOCUMENTATION

------------------
> 1. `POST: /api/users/` 

### Request body

| Name     | Type | Required |
|----------|------|----------|
| username | str  | true     |
| email    | str  | true     |
| password | str  | true     |

### Response example
```
{
    "username": "test1", 
    "email": "test@gmail.com", 
    "id": 1, 
    "created_at": "datetime"
}
```
------------------

> 2. `GET: /api/users/<int:user_id>/`
### Response example
```
{
    "username": "test1", 
    "email": "test@gmail.com", 
    "id": 1, 
    "created_at": "datetime"
}
```
------------------
> 3`POST: /api/auth/` 

### Request body

| Name     | Type | Required |
|----------|------|----------|
| email    | str  | true     |
| password | str  | true     |

### Response example
```
{
    "access_token": "token", 
}
```
------------------
> 4`POST: /api/posts/` 

### Request body

| Name    | Type | Required |
|---------|------|----------|
| title   | str  | true     |
| content | str  | true     |
1. [ ] **HEADERS["AUTHORIZATION"] = "Bearer TOKEN"**
### Response example
```
{
    "title": "test1", 
    "content": "content", 
    "id": 1, 
    "user_id": 1,
    "created_at": "datetime"
}
```
-------------------
> 5. `GET: /api/posts/<int:post_id>/`
### Response example
```
{
    "title": "test1", 
    "content": "content", 
    "id": 1, 
    "user_id": 1,
    "created_at": "datetime"
}
```
------------------
> 6. `GET: /api/posts/`
### Response example
```
[
    {
        "title": "test1", 
        "content": "content", 
        "id": 1, 
        "user_id": 1,
        "created_at": "datetime"
    },
    {
        "title": "test1", 
        "content": "content", 
        "id": 2, 
        "user_id": 1,
        "created_at": "datetime"
    },
]
```
------------------
> 7. `POST: /api/posts/comments/` 

### Request body

| Name    | Type | Required |
|---------|------|----------|
| post_id | int  | true     |
| content | str  | true     |

1. [ ] **HEADERS["AUTHORIZATION"] = "Bearer TOKEN"**
### Response example
```
{
    "post_id": 1, 
    "content": "content", 
    "id": 1, 
    "user_id": 1,
    "created_at": "datetime"
}
```
-------------------
> 8. `GET: /api/posts/comments/<int:post_id>/`
### Response example
```
[
    {
        "post_id": 1, 
        "content": "content", 
        "id": 1, 
        "user_id": 1,
        "created_at": "datetime"
    },
    {
        "post_id": 1, 
        "content": "content", 
        "id": 2, 
        "user_id": 1,
        "created_at": "datetime"
    }
]
```
------------------