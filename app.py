from flask import Flask
from dotenv import load_dotenv
from db import *
import os
from flask_marshmallow import Marshmallow
# This is from hmwk but not sure what yet what it's used for (util (is file).reflection (what is reflection))
# from util.reflection import populate_object

app = Flask(__name__)

load_dotenv()

from models.customer import cust
from models.event_planner import eplanner
from models.event_svcs import eservices
from models.planner_event_xref import planeventxref
from models.venue import venue
from models.auth_tokens import AuthToken

from routes.customer_routes import cust
from routes.event_planner_routes import eplanner
from routes.event_svcs_routes import eservices
from routes.planner_event_xref import planeventxref
from routes.venue_routes import venue
from routes.auth_routes import AuthToken

database_pre = os.environ.get("DATABASE_PRE")
database_user = os.environ.get("DATABASE_USER")
database_addr = os.environ.get("DATABASE_ADDR")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

# Might need to add more to this section
app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_user}@{database_addr}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


init_db(app.db)
ma = Marshmallow(app)

app.register_blueprint(cust)
app.register_blueprint(eplanner)
app.register_blueprint(eservices)
app.register_blueprint(planeventxref)    
app.register_blueprint(venue)
app.register_blueprint(auth)
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(port=8086, host="0.0.0.0", debug=True)
