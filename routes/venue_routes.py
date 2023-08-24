from flask import Blueprint, request
from controllers import venue_controller

venue_routes = Blueprint('venue_routes', __name__)

@venue_routes.route('/venues/add', method=["POST"])
def add_venue():
    return venue_controller.add_venue(request)

@venue_routes.route('/venues/get', methods=["GET"])
def get_all_venues():
    return venue_controller.get_all_venues()  #Why no request here?  

@venue_routes.route('/venues/get/<venue_id>', methods=["GET"])
def get_venue_by_id(venue_id):
    return venue_controller.get_venue_by_id(venue_id) #Why no ,request here?

@venue_routes.route('/venues/update/<id>', methods=["PATCH"])
def update_venue(id):
    return venue_controller.update_venues(request, id) #Why request, id here?

@venue_routes.route('/venues/deactivate/<id>', methods=["PATCH"])
def deactivate_venue(id):
    return venue_controller.deactivate_venue(id)

@venue_routes.route('/venues/activate', methods=["PATCH"])
def activate_venue(id):
    return venue_controller.activate_venue(id)

@venue_routes.route('/venues/delete', methods=["DELETE"])
def delete_venue(id):
    return venue_controller.delete_venue(id)




