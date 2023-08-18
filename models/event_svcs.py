import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from models.event_svcs import EventSvcsSchema
from db import db

class EventSvcs(db.Model):
    __tablename__= "Event Services"
    
    service_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    theme = db.Column(db.String())
    location = db.Column(db.String(), nullable=False)
    service_bid = db.Column(db.Numeric(precision=8, scale=2))
    event_date = db.Column(db.String(), nullable=False)
    activities = db.Column(db.String())
    
    #Need assistance understanding this part when using an XREF table and connecting overall.
    cust_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Customers.cust_id'), nullable=False)
    venue_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Event Services.service_id'), nullable=False)

    def __init__(self, theme, email, location, service_bid, event_date, activities, active):
        self.theme = theme
        self.location = location
        self.service_bid = service_bid
        self.event_date = event_date
        self.activities = activities
        self.active = active

    def new_event_services():
        return EventSvcs("", "", "", "", "", True)
    
class EventSvcsSchema(ma.Schema):
    class Meta:
        fields = ['planner_id', 'phone', 'email', 'password', 'city', 'active']
    EventSvcs = ma.fields.Nested(EventSvcsSchema())

event_service_schema = EventSvcsSchema()
event_services_schema = EventSvcsSchema(ma=True)