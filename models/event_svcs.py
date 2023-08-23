import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
# from models.event_svcs import EventSvcs, event_service_schema, event_services_schema
from models.event_svcs import EventSvcsSchema
# from models.event_planner import EventPlannerSchema
from db import db

class EventSvcs(db.Model):
    __tablename__= "EventServices"
    
    service_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    theme = db.Column(db.String())
    location = db.Column(db.String(), nullable=False)
    service_bid = db.Column(db.Numeric(precision=8, scale=2))
    event_date = db.Column(db.String(), nullable=False)
    activities = db.Column(db.String())

    planner = db.relationship("EventPlanners", secondary="PlannerEventXRef", back_populates = "services")
    

    def __init__(self, theme, location, service_bid, event_date, activities, active):
        self.theme = theme
        self.location = location
        self.service_bid = service_bid
        self.event_date = event_date
        self.activities = activities
        self.active = active

    def new_event_services():
        return EventSvcs("", "", "", "", "", "", "", True)
    
class EventSvcsSchema(ma.Schema):
    class Meta:
        fields = ['service_id', 'theme', 'location', 'service_bid', 'event_date', 'activities', "planner"]
    planner = ma.fields.Nested(EventPlannerSchema)

event_service_schema = EventSvcsSchema()
event_services_schema = EventSvcsSchema(many=True)