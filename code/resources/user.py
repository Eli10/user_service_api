from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Field cannot be blank")
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="Field cannot be blank")
    parser.add_argument('icon',
                        type=str,
                        required=True,
                        help="Field cannot be blank")
    parser.add_argument('preferences',
                        type=str,
                        required=True,
                        help="Field cannot be blank")

    # def get(self,name):
    #     return {'name': name}

    def post(self):
        data = UserRegister.parser.parse_args()
        print(data)

        if UserModel.find_by_username(data['username']):
            return {'message': 'User with username already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': "user created successfully"}, 201


class User(Resource):

    def get(self, name):
        user = UserModel.find_by_username(name)
        if user:
            return user.to_json(), 200
        return {'message':'User not registered'}, 404
