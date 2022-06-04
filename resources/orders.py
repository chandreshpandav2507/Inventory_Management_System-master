from models.orders import OrderModel
from flask_restful import Resource,reqparse,inputs
from flask_jwt import jwt_required

class Order(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('item_id',
        type=int,
        required=True,
        help="This Field Cannot Be Empty!"
    )

    parser.add_argument('date',
        type=inputs.datetime_from_iso8601,
        required=True,
        help="Every order needs a date!"
    )

    # @jwt_required()
    def post(self, id):
        if OrderModel.find_by_id(id):
            return {'message':'Use another id!!'}
        recv_data=Order.parser.parse_args()

        order=OrderModel(recv_data['item_id'],recv_data['date'])

        try:
            order.save_to_db()
        except:
            return {'message':'An Error Occured while inserting!'},500

        return order.json()

    @jwt_required()
    def get(self,id):
        order=OrderModel.find_by_id(id)
        if OrderModel.find_by_id(id):
            return order.json()
        return {'message': 'Order with {} id not placed'.format(id)},404

    @jwt_required()
    def delete(self, id):
        order=OrderModel.find_by_id(id)
        print(order)
        if OrderModel.find_by_id(id):
            order.delete_from_db()
        return {'message':'Order Deleted!!'}


class Orders(Resource):
    def get(self):
        return {'orders':[order.json() for order in OrderModel.query.all()]}