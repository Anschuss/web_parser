from flask import Flask

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

from views import *

app.register_blueprint(general, url_prefix="/")
app.register_blueprint(news, url_prefix="/news")

from views.parsers import run


