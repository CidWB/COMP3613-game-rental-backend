import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db, db
from App.models import User, Staff
from App.controllers import (
    create_customer,
    create_user,
    create_game,
    get_customer,
    create_staff,
    get_all_users_json,
    authenticate,
    get_staff,
    get_game,
    get_rental,
    get_staff,
    create_game,
    get_listing,
    update_staff
)

app = create_app({"SQLALCHEMY_DATABASE_URI":'sqlite:///test_database.db', "TESTING":True, "DEBUG":True})


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = Staff("bob", "bobpass")
        assert user.username == "bob"

    def test_toJSON(self):
        user = Staff("bob", "bobpass")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"bob", "type": 'staff'})
    
    # def test_hashed_password(self):

    # def test_check_password(self):
        

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    create_db(app)
    yield app.test_client()
    db.session.remove()
    db.drop_all()


# def test_authenticate():
    
# def test_create_game():
    
def test_create_user():
    user = create_user("bob", "bobpass")
    userID = get_user(user.id)
    if userID not None:
        print(f"User created: {User.toJSON()}")
    else:
        print("test_create_user() failed")
    
# def test_create_staff():

# def test_staff_create_listing():
    
# def test_staff_confirm_rental():
    
# def test_staff_confirm_return():

# class UsersIntegrationTests(unittest.TestCase):

# tests staff's ability to create rentals in system

# def test_staff_confirm_rental(self):

# def test_staff_confirm_return(self):
  
        

    


        

        

