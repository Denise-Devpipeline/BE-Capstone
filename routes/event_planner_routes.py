from flask import request, Blueprint
from controllers import event_planner_controller

event_planner_routes = Blueprint('event_planner_routes', __name__)

@event_planner_routes.route('/event_planner/add', method=["POST"])
def add_event_planner():
    return event_planner_controller.add_event_planner(request)

@event_planner_routes.route('/event_planner/update/<id>', method=["PATCH"])
def update_event_planner(id):
    return event_planner_controller.update_event_planner(request, id)

@event_planner_routes.route('/event_planner/decativate/<id>', method=["PATCH"])
def deactivate_event_planner(id):
    return event_planner_controller.deactivate_event_planner(request, id)

@event_planner_routes.route('/event_planner/activate/<id>', method=["PATCH"])
def activate_event_planner(id):
    return event_planner_controller.activate_event_planner(request, id)

@event_planner_routes.route('/event_planner/delete/<id>', method=["DELETE"]) 
def delete_event_planner(id):
    return event_planner_controller.delete_event_planner(request, id)