import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
# from controllers.event_planner_controller import EventPlanner
# from models.planner_event_xref import PlannerEventXRefSchema
from db import db

class EventPlanner(db.Model):
    __tablename__= "EventPlanners"

    planner_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phone = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    specialty = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    services = db.relationship("EventServices", secondary="PlannerEventXRef", back_populates = "planner")

    def __init__(self, phone, email, password, specialty, active, services):
        self.phone = phone
        self.email = email
        self.password = password
        self.specialty = specialty
        self.active = active
        self.active = services

    def new_event_planner():
        return EventPlanner("", "", "", "", "", True)
    
class EventPlannerSchema(ma.Schema):
    class Meta:
        fields = ['planner_id', 'phone', 'email', 'password', 'specialty', 'active', "services"]

    services = ma.fields.Nested("EventServices")

event_planner_schema = EventPlannerSchema()
event_planners_schema = EventPlannerSchema(many=True)