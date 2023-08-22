import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db

class PlannerEventXref(db.Model):
    __tablename__ = "PlannerEventXRef"
    ####This doesn't look or feel right.
    #Need assistance understanding this part when using an XREF table.
    planner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('EventPlanners.planner_id'), primary_key=True, nullable=False)
    service_id = db.Column(UUID(as_uuid=True), db.ForeignKey('EventServices.service_id'), primary_key=True, nullable=False)

    
    #Not sure what to put in here yet.
    planner = db.relationship('EventPlanners', back_populates='PlannerEventXRef')
    service = db.relationship('EventServices', back_populates='PlannerEventXRef')

    def __init__(self, planner_id, service_id):
        self.planner_id = planner_id
        self.service_id = service_id
      
        

    def get_new_plannerx():
        return PlannerEventXref("", "")


class PlannerEventXRefSchema(ma.Schema):
    class Meta:
        fields = ['planner_id', 'service_id', 'planner', 'service']

    plannerx = ma.fields.Nested('EventPlannerSchema', only=['phone', 'email', 'password', 'specialty'])
    servicex = ma.fields.Nested('EventSvcsSchema', only=['theme', 'location', 'service_bid', 'event_date', 'activities'])


planner_event_xref_schema = PlannerEventXRefSchema()
planner_events_xref_schema = PlannerEventXRefSchema(many=True)