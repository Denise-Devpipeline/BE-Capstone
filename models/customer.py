import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
import uuid
# from models.customer import Customer
from models.event_svcs import EventSvcsSchema
from db import db


class Customer(db.Model):
    __tablename__= "Customer"

    cust_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    event_date = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, first_name, last_name, phone, email, password, city, state, event_date, active):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.city = city
        self.state = state
        self.event_date = event_date
        self.active = active

    def new_customer():
        return Customer("", "", "", "", "", "", "", "", True)
    
class CustomersSchema(ma.Schema):
    class Meta:
        fields = ['cust_id', 'first_name', 'last_name', 'phone', 'email', 'password', 'city', 'state',  "event_date", 'active']
    eventServices = ma.fields.Nested(EventSvcsSchema)

customer_schema = CustomersSchema()
customers_schema = CustomersSchema(many=True)