# Library Management API

## Overview

The **Library Management API** is a RESTful API built using **Django** and **Django Rest Framework (DRF)**. This API allows for easy management of a library system, enabling users to perform CRUD operations on books. It also includes features like rate limiting to prevent abuse and pagination to handle large collections of books.

## Features

- **CRUD Operations** for managing books
  - Retrieve a list of all books
  - Get details of a specific book
  - Add, update, or delete books
- **Rate Limiting** to restrict the number of requests per client
- **Pagination** to manage large collections of books





### Prerequisites

Before getting started, make sure you have the following tools installed:

- Python 3.6+
- Django 3.0+
- Django Rest Framework
- PostgreSQL/MySQL/SQLite (based on your choice of database)


### API Endpoints
1. GET /api/v1/books/
Description: Retrieve a list of all books in the library.

2. GET /api/v1/books/{id}/
Description: Retrieve details of a specific book by ID.

3. POST /api/v1/books/
Description: Create a new book in the library.

4. PUT /api/v1/books/{id}/
Description: Update details of an existing book.

5. DELETE /api/v1/books/{id}/
Description: Delete a book from the library.

Rate Limiting
Purpose: To prevent abuse and ensure fair usage, rate limiting is implemented to restrict the number of requests a client can make in a specific time period.
Rate Limit: 100 requests per minute per client/IP.
Headers in Response:
X-RateLimit-Limit: Total number of allowed requests.
X-RateLimit-Remaining: Remaining requests in the current window.
X-RateLimit-Reset: When the limit will reset (Unix timestamp).
Pagination
To manage large collections of books efficiently, pagination is used. By default, only 2 books will be returned per page. You can use the page query parameter to navigate through different pages.

Example:

GET /api/v1/books/?page=2 to get the second page of results.
Custom Throttling
The API uses CustomRateThrottle to implement custom rate limiting logic. This ensures that clients can only make a limited number of requests per minute. The rate limiting headers (such as X-RateLimit-Remaining and X-RateLimit-Reset) will be included in the API response to guide the client on their usage.

