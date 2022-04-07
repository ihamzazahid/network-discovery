from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
cors = CORS(app, supports_credentials=True)

api = Api(app)

app.secret_key = 'nets-discovery'
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"



app.config['CORS_HEADERS'] = 'Content-Type'

from app.routes import natlas_cli
