# Superheroes API

This project is a simple Flask API that manages superheroes and their powers using a SQLite database. You can create, read, update, and delete heroes, powers, and the relationships between them.

## Table of Contents
- Installation  installation
- Running the Application   running-the-application
- API Endpoints  api-endpoints
  - Heroes  heroes
  - Powers powers
  - Hero Powers hero-powers
- Using Curl  using-curl

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   pip install Flask Flask-SQLAlchemy

   To run the application, execute the following command in your terminal:
   python app.py

   By default, the app will run on http://127.0.0.1:5000.

API Endpoints
Heroes
GET /heroes: Retrieve all heroes.
GET /heroes/<id>: Retrieve a specific hero by ID.
DELETE /heroes/<id>: Delete a specific hero by ID.
Powers
GET /powers: Retrieve all powers.
GET /powers/<id>: Retrieve a specific power by ID.
PATCH /powers/<id>: Update a specific power's description by ID.
DELETE /powers/<id>: Delete a specific power by ID.
Hero Powers
POST /hero_powers: Create a relationship between a hero and a power.
GET /hero_powers: Retrieve all hero powers.
DELETE /hero_powers/<id>: Delete a specific hero power by ID.
Using Curl
You can use curl commands in your terminal to interact with the API. Below are some examples:

1. Fetch All Heroes
CopyReplit
curl http://127.0.0.1:5000/heroes
2. Fetch a Specific Hero by ID
To fetch a hero with ID 1:

CopyReplit
curl http://127.0.0.1:5000/heroes/1
3. Fetch All Powers
CopyReplit
curl http://127.0.0.1:5000/powers
4. Fetch a Specific Power by ID
To fetch a power with ID 1:

CopyReplit
curl http://127.0.0.1:5000/powers/1
5. Update a Power Description
To update the description of a power with ID 1:

CopyReplit
curl -X PATCH http://127.0.0.1:5000/powers/1 -H "Content-Type: application/json" -d '{"description": "New description for power."}'
6. Create a Hero Power
To create a new hero power relationship:

CopyReplit
curl -X POST http://127.0.0.1:5000/hero_powers -H "Content-Type: application/json" -d '{"hero_id": 1, "power_id": 1, "strength": "Strong"}'
7. Fetch All Hero Powers
CopyReplit
curl http://127.0.0.1:5000/hero_powers
8. Delete a Hero Power by ID
To delete a hero power with ID 1:

CopyReplit
curl -X DELETE http://127.0.0.1:5000/hero_powers/1
9. Delete a Power by ID
To delete a power with ID 1:

CopyReplit
curl -X DELETE http://127.0.0.1:5000/powers/1
10. Delete a Hero by ID
To delete a hero with ID 1:

CopyReplit
curl -X DELETE http://127.0.0.1:5000/heroes/1

for postman 
API Management with Postman
This section provides a guide on how to use Postman to interact with the API for managing Heroes, Powers, and Hero Powers.

Base URL
All requests are made to the following base URL:

Get All Heroes

HTTP Method: GET
Endpoint: /heroes
Description: Retrieves a list of all heroes.
CopyReplit
GET http://127.0.0.1:5000/heroes

Get a Specific Hero by ID

HTTP Method: GET
Endpoint: /heroes/<hero_id>
Description: Retrieves details of a specific hero using their ID.
CopyReplit
GET http://127.0.0.1:5000/heroes/1

Get All Hero Powers

HTTP Method: GET
Endpoint: /hero-powers
Description: Retrieves a list of all hero powers.
CopyReplit
GET http://127.0.0.1:5000/hero-powers

Get a Specific Hero Power by ID

HTTP Method: GET
Endpoint: /hero-powers/<power_id>
Description: Retrieves details of a specific hero power using its ID.
CopyReplit
GET http://127.0.0.1:5000/hero-powers/1

Get All Powers

HTTP Method: GET
Endpoint: /powers
Description: Retrieves a list of all available powers.
CopyReplit
GET http://127.0.0.1:5000/powers

Get a Specific Power by ID

HTTP Method: GET
Endpoint: /powers/<power_id>
Description: Retrieves details of a specific power using its ID
CopyReplit
GET http://127.0.0.1:5000/powers/1

