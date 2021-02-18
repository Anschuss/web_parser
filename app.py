from flask import Flask

from kombu import serialization
from config import make_celery, Configuration

from flask_sqlalchemy import SQLAlchemy

### Flask###

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

### Celery ###


client = make_celery(app)
client.conf.update(app.config)

### Blueprints ###

from vews import *

app.register_blueprint(general, url_prefix="/")
app.register_blueprint(news, url_prefix="/news")

from vews.parsers import run


