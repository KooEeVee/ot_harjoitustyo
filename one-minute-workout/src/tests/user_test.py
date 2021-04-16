import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testname", "1234")

    def test_user_exists(self):
        self.assertNotEqual(self.user, None)

    def test_username_is_correct(self):
        self.assertEqual(str(self.user), "username: testname")
