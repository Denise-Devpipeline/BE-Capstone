import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
from customer import CustomersSchema

#

class AuthTokens(db.Model):
    __tablename__ = "AuthTokens"

    auth_token = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Customers.cust_id"), nullable=False)
    #Would the planner id also go on here?  
    expiration = db.Column(db.DateTime, nullable=False)

    def __init__(self, cust_id, expiration):
        self.cust_id = cust_id
        self.expiration = expiration


class AuthTokenSchema(ma.Schema):
    class Meta:
        fields = ['auth_tokens', 'cust_id', 'expiration']

######Need help to understand this part.  Is this where I would add a role?  Where else would the role be? on the ERD, on tables in models? 
    customer = ma.fields.Nested(CustomersSchema(only=("something", "something")))


auth_token_schema = AuthTokenSchema()
