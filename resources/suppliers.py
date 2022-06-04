from models.suppliers import SupplierModel
from flask_restful import reqparse,Resource
from flask_jwt import jwt_required

class Supplier(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('mobile_no',
        type=int,
        required=True,
        help="You must Enter the mobile number of the supplier!!"
    )

    # @jwt_required()
    def post(self,name):
        if SupplierModel.find_by_name(name):
            return {"message":"{} Already Exists!!".format(name)},400
        recv_data=Supplier.parser.parse_args()
        supplier=SupplierModel(name,recv_data['mobile_no'])

        try:
            supplier.save_to_db()
        except:
            return {"message":"An error Occured while inserting the data!!"},500
        return supplier.json(),201

    @jwt_required()
    def get(self,name):
        supplier=SupplierModel.find_by_name(name)
        if supplier:
            return supplier.json()
        return {"message":"Supplier Not Found in your Record!!!"}

    @jwt_required()
    def delete(self,name):
        supplier=SupplierModel.find_by_name(name)
        if supplier:
            supplier.delete_from_db()
        return {"message":"Supplier Deleted"}
    
class Suppliers(Resource):
    def get(self):
        return {'suppliers':[supplier.json() for supplier in SupplierModel.query.all()]}
            