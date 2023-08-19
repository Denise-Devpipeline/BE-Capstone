from flask import request, Blueprint
from controllers import event_svcs_controller

event_svcs_routes = Blueprint('event_svcs_routes', __name__)

@event_svcs_routes.route('/event_services/add', method=["POST"])
def add_event_services():
    return event_svcs_controller.add_event_services(request)

