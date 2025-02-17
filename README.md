# Optimizing web application performance

## Introduction

This document provides a brief overview of the performance optimization techniques that can be used to improve the performance of a web application.

1. [Using Flask and Redis to optimize web application performance]
   (https://medium.com/@fahadnujaimalsaedi/using-flask-and-redis-to-optimize-web-application-performance-34a8ae750097)

## Technologies

- Python
- Flask
- Redis
  -Sqlite3

## Installation

To run this project, you need to have Python installed on your local machine. You can download Python from the official website. You also need to install Flask and Redis. You can install Flask using the following command:

```bash
pipenv install Flask flask-redis flask-sqlalchemy sqlalchemy-serializer
```

## Running the application

To run the application, you need to execute the following command:

```bash
flask run --debug --port 5080
```

## Seed the database

To seed the database, you need to execute the following command:

```bash
python3 seed.py
```

## Testing the application use thunder client or postman

To test the application, you can use Thunder Client or Postman. You can send a POST request to the following URL:

```bash
http://localhost:5080/items
```

## Conclusion

For more information, please refer to the article mentioned above.