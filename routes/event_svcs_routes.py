from flask import request, Blueprint
from controllers import event_svcs_controller

event_svcs_routes = Blueprint('event_svcs_routes', __name__)

@event_svcs_routes.route('/event_services/add', method=["POST"])
def add_event_services():
    return event_svcs_controller.add_event_services(request)

@event_svcs_routes.route('/event_services/planner/<planner_id>', method=["GET"])
def get_event_by_planner_id(planner_id):
    return event_svcs_controller.get_event_by_planner_id(planner_id)

@event_svcs_routes.route('/event_services/update/<id>', method=["PATCH"])
def update_event_services(id):
    return event_svcs_controller.update_event_service(id)

@event_svcs_routes.route('/event_services/deactivate/<id>', method=["PATCH"])
def deactivate_event_service(id):
    return event_svcs_controller.deactivate_event_service(id)

@event_svcs_routes.route('/event_services/activate/<id>', method=["PATCH"])
def activate_event_service(id):
    return event_svcs_controller.activate_event_service(id)

@event_svcs_routes.route('/event_services/delete/<id>', method=["DELETE"])
def delete_event_service(id):
    return event_svcs_controller.delete_event_service(id)
    
    
