from flask import Flask
from routes import event_services_routes
from db import *

import os
from flask_marshmallow import Marshmallow

app = Flask(__name__)


# Why do I need these SCHEMAS written this way? (2 schemas each)
from models.customer import Customer, customer_schema, customers_schema
from models.event_planner import EventPlanner, event_planner_schema, event_planners_schema
from models.event_svcs import EventSvcs, event_svcs_schema, event_svc_schema
from models.planner_event_xref import PlannerEventXref, planner_event_xref_schema, planner_event_xrefs_schema
from models.venue import Venue, venue_schema, venues_schema
from models.auth_tokens import AuthToken, auth_tokens_schema

# This is from hmwk but not sure what yet what it's used for (util (is file).reflection (what is reflection))
from util.reflection import populate_object

from routes.customer_routes import cust
from routes.event_planner_routes import eplanner
from routes.event_svcs_routes import eservices
from routes.planner_event_xref import planeventxref
from routes.venue_routes import venue

database_pre = os.environ.get("DATABASE_PRE")
database_user = os.environ.get("DATABASE_USER")
database_addr = os.environ.get("DATABASE_ADDR")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

# Might need to add more to this section
app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_user}@{database_addr}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


init_db(app.db)
ma = Marshmallow(app)

app.register_blueprint(Customer)
app.register_blueprint(EventPlanner)
app.register_blueprint(EventSvcs)  #OR what is on line 47
app.register_blueprint(event_services_routes, url_prefix='/event_services')
app.register_blueprint(Venue)
# Does auth belong in here?
app.register_blueprint(Auth)
