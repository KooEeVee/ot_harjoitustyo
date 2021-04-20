import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testname", "1234")

    def test_user_exists(self):
        self.assertNotEqual(self.user, None)

    def test_username_is_correct(self):
        self.assertEqual(str(self.user), "username: testname")

    def test_user_added_to_csv(self):
        self.user.new_user_csv()
        self.assertEqual(self.user.get_username_csv(self.user.username),True)
        self.assertEqual(self.user.get_password_csv(self.user.username),self.user.password)