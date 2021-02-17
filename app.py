from flask import Flask
from kombu import serialization

from config import make_celery, Configuration


serialization.registry._decoders.pop("application/x-python-serialize")

app = Flask(__name__)
app.config.from_object(Configuration)

from general import general

app.register_blueprint(general, url_prefix="/")

from nplus import n_plus

app.register_blueprint(n_plus, url_prefix="/n_plus")


client = make_celery(app)
client.conf.update(app.config)
