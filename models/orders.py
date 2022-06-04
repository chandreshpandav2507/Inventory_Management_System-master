from db import db
from flask import jsonify

class OrderModel(db.Model):
    __tablename__='orders'

    id=db.Column(db.Integer, primary_key=True)
    
    item_id=db.Column(db.Integer, db.ForeignKey('items.id'))
    item=db.relationship('ItemModel')

    date=db.Column(db.String(80))

    def __init__(self, item_id, date):

        self.item_id=item_id
        self.date=date

    def json(self):
        return {'item_id':self.item_id, 'date':self.date}

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
