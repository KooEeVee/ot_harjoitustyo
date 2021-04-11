import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        username = "testname"
        self.user = User(username)

    def test_user_exists(self):
        self.assertNotEqual(self.user, None)

    def test_username_is_correct(self):
        self.assertEqual(str(self.user), "username: testname")