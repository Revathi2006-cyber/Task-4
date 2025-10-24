  # Flask REST API - Task 4

  ## Project Structure
  flask-api
  
  │
  
  ├── app.py      # Main Flask application with API routes
  
  ├── .venv/      # Virtual environment folder (not pushed to GitHub)
  
  └── README.md   # Project documentation

  ## API Endpoints

  The API manages users stored in an in-memory dictionary.

  ### 1️⃣ Create User (POST)
  - URL: /users
  - Method: POST
  - Body (JSON):
    {
      "id": "1",
      "name": "Revathi",
      "email": "rev@example.com"
    }
  - Response:
    {
      "message": "User Created",
      "user": {
        "id": "1",
        "name": "Revathi",
        "email": "rev@example.com"
      }
    }

  ### 2️⃣ Get All Users (GET)
  - URL: /users
  - Method: GET
  - Response:
    {
      "1": {
        "id": "1",
        "name": "Revathi",
        "email": "rev@example.com"
      }
    }

  ### 3️⃣ Get Single User (GET)
  - URL: /users/<user_id>
  - Method: GET
  - Response:
    {
      "id": "1",
      "name": "Revathi",
      "email": "rev@example.com"
    }

  ### 4️⃣ Update User (PUT)
  - URL: /users/<user_id>
  - Method: PUT
  - Body (JSON):
    {
      "name": "Revathi Updated"
    }
  - Response:
    {
      "message": "User Updated",
      "user": {
        "id": "1",
        "name": "Revathi Updated",
        "email": "rev@example.com"
      }
    }

  ### 5️⃣ Delete User (DELETE)
  - URL: /users/<user_id>
  - Method: DELETE
  - Response:
    {
      "message": "User Deleted",
      "user": {
        "id": "1",
        "name": "Revathi Updated",
        "email": "rev@example.com"
      }
    }

  ## How to Run the Project

  Navigate to the project folder:
  cd flask-api

  Create and activate virtual environment:
  python -m venv .venv
  # Windows (PowerShell)
  .\.venv\Scripts\Activate.ps1
  
  source .venv/bin/activate

  Install Flask:
  pip install flask

  Run the Flask app:
  python app.py

  Test API in Postman:
  Open Postman and use the URL:
  http://127.0.0.1:5000

  ## Outcome
  - Learned REST API fundamentals
  - Built CRUD operations using Flask
  - Practiced testing APIs using Postman
