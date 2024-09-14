# API Server Assignment

## Project Overview

This project implements an API server that supports GraphQL queries to fetch bank branch data. The API is built using Django and is hosted on AWS. This README outlines the solution approach, technologies used, and deployment details.

## Features

- **GraphQL Endpoint**: Available at `/gql` for querying bank branch data.
- **Data Query**: Supports a query to retrieve bank branches along with related subclass data.
- **Deployment**: Hosted on AWS.

## Sample GraphQL Query

Use the following query to fetch bank branch data:

```graphql
query {
  branches {
    edges {
      node {
        branch
        bank {
          name
        }
        ifsc
      }
    }
  }
}
```
## Technologies Used
- **Framework**: Django
- **GraphQL Library**: Graphene-Django
- **Database**: PostgreSQL
- **Deployment**: AWS (URL: ```http://54.234.60.172:8000/gql/```)

## Setup Instructions
**Clone the Repository**:

```
git clone https://github.com/safvan001/bank_api.git
cd bank_api
```
**Install Dependencies**:
```
pip install -r requirements.txt
```
**Run Migrations**:
```
python manage.py migrate
```
**Start the Server**:
```
python manage.py runserver
```
**Deployment**:
The project is deployed on AWS. The endpoint is available at: ```http://54.234.60.172:8000/gql/ ```.

