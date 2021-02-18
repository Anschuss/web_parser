import datetime
class Configuration(object):
    DEBUG = True
    SECRET_KEY = "4e90b165e5e5380b"

    ### Postgres ####
    SQLALCHEMY_DATABASE_URI = "postgres+psycopg2://user:password@0.0.0.0:5432/news"

    ### CELERY CONFIG ###

    CELERY_BROKER_URL = 'redis://0.0.0.0:6379',
    CELERY_RESULT_BACKEND = 'redis://0.0.0.0:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_SOFT_TIME_LIMIT = 120
    CELERY_TIME_LIMIT = 240

    CELERYBEAT_SCHEDULE = {
        'task-name': {
            'task': 'vews.parsers.run_pars.run',  # instead 'show'
            'schedule': datetime.timedelta(hours=3),
        },
    }

    CELERY_TIMEZONE = 'UTC'