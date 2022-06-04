from db import db

class SupplierModel(db.Model):
    __tablename__='suppliers'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    mobile_no=db.Column(db.Integer)

    def __init__(self,name,mobile_no):
        self.name=name
        self.mobile_no=mobile_no

    def json(self):
        return {'name': self.name,'mobile_no':self.mobile_no}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()