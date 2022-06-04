from db import db

class PurchaseModel(db.Model):

    __tablename__='purchases'

    id=db.Column(db.Integer, primary_key=True)

    supplier_id=db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    supplier=db.relationship('SupplierModel')

    item_id=db.Column(db.Integer, db.ForeignKey('items.id'))
    item=db.relationship('ItemModel')

    recieved=db.Column(db.Boolean)
    date=db.Column(db.String)

    def __init__(self, supplier_id, item_id, recieved, date):
        self.supplier_id=supplier_id
        self.item_id=item_id
        self.recieved=recieved
        self.date=date

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def json(self):
        return {'recieved':self.recieved, 'date': self.date, 'supplier':self.supplier.json(), 'item':self.item.json()}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



