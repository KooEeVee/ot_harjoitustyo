import unittest
from user import User
from timer import Timer


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testname", "1234")
        #self.timer = Timer("10:10", "20:20", "30", "testname")

    def test_user_exists(self):
        self.assertNotEqual(self.user, None)

    def test_user_is_saved_in_json(self):
        self.user.new_user_json()
        self.assertEqual(self.user.get_user_json(), True)

    def test_user_password_is_correct_in_json(self):
        self.assertEqual(self.user.get_password_json("testname"), "1234")

    
    # def test_user_added_to_csv(self):
    #     self.user.new_user_csv()
    #     self.assertEqual(self.user.get_username_csv(self.user.username), True)
    #     self.assertEqual(self.user.get_password_csv(
    #         self.user.username), self.user.password)
