# User Service Api

Currently just adds users to a db and can search for users based on username and id. More will be implemented soon

## Setup

Set up Python 3 Virtual environment 
- pip install virtualenv
- virutalenv venv --python=python3

Install all Dependencies
- pip install -r requirements.txt
- cd code
- In the code directory, run app.py


## Sample Request

curl -X POST \
  http://127.0.0.1:5000/user \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{

	"username":"Eli10",
	"password":"1234",
	"location": "NY",
	"icon": "pepe.jpg",
	"preferences": "pizza,juice"

}'
