from flask import Flask
from kombu import serialization
from config import make_celery, Configuration

### Flask###

app = Flask(__name__)
app.config.from_object(Configuration)

### Celery ###

serialization.registry._decoders.pop("application/x-python-serialize")
client = make_celery(app)
client.conf.update(app.config)

### Blueprints ###

from general import general
from dw import dw_page
from nplus import n_plus
from bbc import bbc
from spiegel import spiegel
app.register_blueprint(general, url_prefix="/")
app.register_blueprint(n_plus, url_prefix="/n_plus")
app.register_blueprint(bbc, url_prefix="/bbc")
app.register_blueprint(dw_page, url_prefix="/dw")
app.register_blueprint(spiegel, url_prefix="/spiegel")