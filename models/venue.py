import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from models.venue import VenueSchema
from db import db

class Venue(db.Model):
    __tablename__= "Venues"

    venue_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    venue_name = db.Column(db.String(), nullable=False)
    venue_address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    accomodations = db.Column(db.String())
    seasons = db.Column(db.String())

    active = db.Column(db.Boolean(), default=True)

    
    #Need assistance understanding this part when using an XREF table.
    service_id = db.Column(UUID(as_uuid=True), db.ForeignKey("EventServices.service_id"), nullable=False)


    def __init__(self, venue_name, venue_address, phone, email, accomodations, seasons, active):
        self.venue_name = venue_name
        self.venue_address = venue_address
        self.phone = phone
        self.email = email
        self.accomodations = accomodations
        self.seasons = seasons
        self.active = active

    def new_venue():
        return Venue("", "", "", "", "", True)
    
class VenueSchema(ma.Schema):
    class Meta:
        fields = ['venue_id', 'venue_name', 'venue_address', 'phone', 'email', "accomodaitons", 'seasons', 'active']
    venue = ma.fields.Nested(VenueSchema)

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)