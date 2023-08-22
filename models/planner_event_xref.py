import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db

class PlannerEventXref(db.Model):
    __tablename__ = "PlannerEventXRef"
    ####This doesn't look or feel right.
    #Need assistance understanding this part when using an XREF table.
    planner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Service.service_id'), primary_key=True, nullable=False)
    service_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Planner.planner_id'), primary_key=True, nullable=False)

    #Need assistance understanding this part when using an XREF table.  What about db.relationship('EventSvcs', backref=db.backref('EventPlanner', lazy=True )
    service_id = db.Column(UUID(as_uuid=True), db.ForeignKey("EventServices.event_id"), nullable=False) #Think this on is incorrect.

    #Not sure what to put in here yet.
    something = db.relationship('Something', back_populates='PlannerEventXRef')

    def __init__(self, planner_id, service_id):
        self.planner_id = planner_id
        self.service_id = service_id
      
        

    def get_new_plannerx():
        return PlannerEventXref("", "")


class PlannerEventXRefSchema(ma.Schema):
    class Meta:
        fields = ['planner_id', 'service_id']

    #Saw this on an example and not sure what it has to do with anything here.???
    plannerx = ma.fields.Nested('PlannerEventXRefSchema')


planner_event_xref_schema = PlannerEventXRefSchema()
planner_events_xref_schema = PlannerEventXRefSchema(many=True)