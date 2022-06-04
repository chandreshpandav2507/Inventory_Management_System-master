from models.users import UserModel
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class User_Registered(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=True,
        help="Username must be provided!!!"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="Password must be provided!!!"
    )

    def post(self):
        recv_data=User_Registered.parser.parse_args()

        if UserModel.find_by_name(recv_data['username']):
            return {"message":"A user with {} name already registered!".format(recv_data['username'])},400

        user=UserModel(recv_data['username'],recv_data['password'])
        user.save_to_db()

        return {"message":"User Registered Successfully!"},201




    
