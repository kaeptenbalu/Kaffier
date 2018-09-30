from app import db

class Product(db.Model):
    __tablename__ = "EK"

    ID = db.Column(db.Integer, primary_key=True)
    Produkt = db.Column(db.TEXT, nullable=False)
    Vorhanden = db.Column(db.Integer)
    Krit = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Product: {}>'.format(self.name)

class Beer(db.Model):
    __tablename__ = "Bier"

    id = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.TEXT, nullable=False)
    Anzahl = db.Column(db.Integer)
    Strichcode = db.Column(db.String(255))

    def __repr__(self):
        return '<Beer: {}>'.format(self.name)

class Senseo(db.Model):
    __tablename__ = "Kaffeemaschine"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.Boolean)
