from flask import Blueprint

from counter.models import Counter # To know that are some db defintions in this application
from application import db

counter_app = Blueprint('counter_app', __name__)

@counter_app.route('/')
def init():
    counter = Counter.query.first() # fetch the first counter object
    if not counter:
        counter = Counter(1) # why can you just enter 1 directly here without a variable? 
        db.session.add(counter)
        db.session.commit()
    else:
        counter.count += 1
        db.session.commit()
    return '<h1>Counter: ' + str(counter.count) + '</h1>'
