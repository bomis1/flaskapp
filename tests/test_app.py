# Import the necessary modules
#from flask import url_for
from flask import *
#from flask_testing import TestCase
from flask_testing import *

# import the app's classes and objects
from app import app, db, Team, Player 

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()

        # Create test team
        sample1 = Team(team_name="Arsenal")
        sample2 = Player(name="Ronaldo")

        # save users to database
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Arsenal', response.data)

    # def test_player_get(self):
    #     response = self.client.get(url_for('players'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Christiano Ronaldo', response.data)
       

    # def test_home_delete(self):
    #     response = self.client.post('/players/2/delete')
    #     self.assertEqual(response.status_code, 200)
        
        
