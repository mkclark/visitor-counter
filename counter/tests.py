import os
import unittest # python's builtin testing library
import pathlib

from dotenv import load_dotenv # need to manually import the .flaskenv file as it's being run directly by python and not by Flask
env_dir = pathlib.Path(__file__).parents[1]
load_dotenv(os.path.join(env_dir, '.flaskenv'))

from counter.models import Counter
from application import db
from application import create_app as create_app_base # creating a new create_app method in the test
from utils.test_db import TestDB

class CounterTest(unittest.TestCase):
    def create_app(self):
        return create_app_base(
            SQLALCHEMY_DATABASE_URI=self.db_uri,
            TESTING=True,
            SECRET_KEY = 'mySecret!'
        )

    def setUp(self):
        self.test_db = TestDB()
        self.db_uri = self.test_db.create_db()
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()
        with self.app_factory.app_context():
            db.create_all()

    def tearDown(self):
        with self.app_factory.app_context():
           db.drop_all()
        self.test_db.drop_db()

    def test_counter(self): # The first test
        rv = self.app.get('/')  # hitting the index URL
        assert '1' in str(rv.data) # store output in the 'rv' variable
        rv = self.app.get('/')
        assert '2' in str(rv.data)
