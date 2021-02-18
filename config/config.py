class Configuration(object):
    DEBUG = True
    SECRET_KEY = "4e90b165e5e5380b"

    ### CELERY CONFIG ###

    CELERY_BROKER_URL = 'amqp://async_python:12345@0.0.0.0:6379'
    CELERY_RESULT_BACKEND = 'amqp://async_python:12345@0.0.0.0:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_SOFT_TIME_LIMIT = 120
    CELERY_TIME_LIMIT = 240