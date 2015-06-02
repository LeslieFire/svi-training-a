from datetime import timedelta

BROKER_URL = 'amqp://localhost//'
CELERY_RESULT_BACKEND = 'db+postgresql://localhost/celery-beat-db'

CELERYBEAT_SCHEDULE = {
    'every-second': {
        'task': 'tasks.add',
        'schedule':timedelta(seconds=1),
        'args':(51,52),
    },
}
