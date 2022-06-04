from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.users import User_Registered
from resources.item import Item, Items
from resources.suppliers import Supplier, Suppliers
from resources.orders import Order, Orders
from resources.purchases import Purchase, Purchases

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='Riddhi'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)

api.add_resource(User_Registered,'/register')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(Supplier,'/supplier/<string:name>')
api.add_resource(Suppliers,'/suppliers')
api.add_resource(Order,'/order/<int:id>')
api.add_resource(Orders, '/orders')
api.add_resource(Purchase, '/purchase/<int:id>')
api.add_resource(Purchases, '/purchases')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
app.run(port=5935,debug=True)

