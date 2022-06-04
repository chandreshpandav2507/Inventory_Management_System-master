from models.purchases import PurchaseModel
from flask_restful import Resource, reqparse, inputs
from flask import request
from flask_jwt import jwt_required

class Purchase(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('supplier_id',
        type=int,
        required=True,
    help="Every purchase needs a supplier id!"
    )

    parser.add_argument('received',
        type=int,
        required=True,
        help="This field cannot be Empty!"
    )

    parser.add_argument('date',
        type=inputs.datetime_from_iso8601,
        required=True,
        help="This field cannot be Empty!"
    )

    parser.add_argument('item_id',
        type=int,
        required=True,
        help="Please Enter Item id!"
    )

    # @jwt_required()
    def post(self, id):
        if PurchaseModel.find_by_id(id):
            return {'message':'A purchase with this id already exists'},400

        reciv_data=Purchase.parser.parse_args()
        # reciv_data=request.get_json()

        purchase=PurchaseModel(reciv_data['supplier_id'], reciv_data['item_id'], reciv_data['received'], reciv_data['date'])

        try:
            purchase.save_to_db()
        except:
            return {"message":"An Error Occured while inserting a purchase!"},500 #internal server error
        
        return purchase.json(),201

    @jwt_required()
    def get(self, id):
        purchase=PurchaseModel.find_by_id(id)
        if PurchaseModel.find_by_id(id):
            return purchase.json()
        return {'message': 'Purchase with {} id not placed'.format(id)},404

    @jwt_required()
    def delete(self, id):
        purchase=PurchaseModel.find_by_id(id)
        print(purchase)
        if PurchaseModel.find_by_id(id):
            purchase.delete_from_db()
        return {'message':'Purchase Record Deleted!!'}


class Purchases(Resource):
    def get(self):
        return {'purchases':[purchase.json() for purchase in PurchaseModel.query.all()]}
