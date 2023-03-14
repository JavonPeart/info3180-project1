from . import db
from werkzeug.security import generate_password_hash



class Property(db.Model):
    __tablename__ = 'property_data'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    location = db.Column(db.String(80))
    price = db.Column(db.String(80))
    type = db.Column(db.String(80))
    description = db.Column(db.String(200))
    photo = db.Column(db.String(80))

    def __init__(self, title, bedrooms, bathrooms, location, price, type, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo

    def is_authenticated(self):
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support