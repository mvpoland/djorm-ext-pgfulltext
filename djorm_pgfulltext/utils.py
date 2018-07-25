import psycopg2

from django.db import connection
from django.utils.text import force_text


def adapt(text):
    a = psycopg2.extensions.adapt(force_text(text))
    c = connection.connection

    # This is a workaround for:
    # https://szeryf.mvpl.eu/sentry/mv-demo/issues/7946/
    if hasattr(c, '__wrapped__'):
          c = getattr(c, '__wrapped__')
    a.prepare(c)
    return a
