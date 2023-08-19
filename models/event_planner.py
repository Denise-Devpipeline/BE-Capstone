import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from models.event_planner import EventPlannerSchema
from db import db

class EventPlanner(db.Model):
    __tablename__= "Event Planners"

    planner_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phone = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    specialty = db.Column(db.String(), nullable=False)
    
    #Need assistance understanding this part when using an XREF table.  What about db.relationship('EventSvcs', backref=db.backref('EventPlanner', lazy=True )
    service_id = db.Column(UUID(as_uuid=True), db.ForeignKey("EventServices.event_id"), nullable=False)

    active = db.Column(db.Boolean(), default=True)

    def __init__(self, phone, email, password, specialty, active):
        self.phone = phone
        self.email = email
        self.password = password
        self.city = specialty
        self.active = active

    def new_event_planner():
        return EventPlanner("", "", "", "", "", True)
    
class EventPlannerSchema(ma.Schema):
    class Meta:
        fields = ['planner_id', 'phone', 'email', 'password', 'city', 'active']
    EventPlanner = ma.fields.Nested(EventPlannerSchema())

event_planner_schema = EventPlannerSchema()
event_planners_schema = EventPlannerSchema(ma=True)