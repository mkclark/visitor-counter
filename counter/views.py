from flask import Blueprint

from counter.models import Counter # To know that are some db defintions in this application

counter_app = Blueprint('counter_app', __name__)

@counter_app.route('/')
def init():
    return 'Counter App'
