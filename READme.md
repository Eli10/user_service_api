# User Service Api

Currently just adds users to a db and can search for users based on username and id. More will be implemented soon

## Setup

Have python and pip installed on machine
- pip install -r requirements.txt

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
