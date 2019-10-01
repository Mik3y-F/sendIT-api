from app import db

class User(db.Model):
    """This class represents the users table."""

    __tablename__: str = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    mobileNo = db.Column(db.String(255))
    email = db.Column(db.String(255))
    isAdmin = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)


class Parcel(db.Model):
    """This class represents the parcels table."""

    __tablename__: str = 'parcels'

    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    orderDate = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    orderStatus = db.Column(db.String(255))
    presentLocation = db.Column(db.String(255))
    pickupLocation = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Parcel.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Parcel: {}>".format(self.id)


class OrderStatus(db.Model):
    """This class represents the sources table."""

    __tablename__: str = 'order_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return OrderStatus.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<OrderStatus: {}>".format(self.status)