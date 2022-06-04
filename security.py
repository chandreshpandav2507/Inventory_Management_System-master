from models.users import UserModel

def authenticate(username,password):
    user=UserModel.find_by_name(username)

    if user and user.password==password:
        return user

def identity(payload):
    id=UserModel.find_by_id(payload['identity'])
    return id