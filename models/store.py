import sqlite3
from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name,
                'items': [item.json() for item in self.items.all()] }

    @classmethod
    def find_by_name(cls, name):
        # select * from tablename where name = name
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # 'INSERT INTO items VALUES(?,?)'
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # UPDATE items SET price=? WHERE name=?
        db.session.delete(self)
        db.session.commit()
