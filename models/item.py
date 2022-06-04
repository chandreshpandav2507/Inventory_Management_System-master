from db import db

class ItemModel(db.Model):
    __tablename__='items'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))

    orders=db.relationship('OrderModel', lazy='dynamic')
    #purchase=db.relationship('PurchaseModel')

    def __init__(self, name, price):
        self.name=name
        self.price=price

    def json(self):
        return {'name': self.name,'price': self.price, 'orders':[order.json() for order in self.orders.all()]} #,'purchase':self.purchase.json()}

    # def purchase_item(self):
    #     return {'purchases': }

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
