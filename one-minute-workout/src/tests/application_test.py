# import unittest
# from os import path
# from application import Application

# class TestApplication(unittest.TestCase):
#     def setUp(self):
#         self.application = Application()
#         self.application.initialize_users_json()
#         self.application.initialize_ui()
#         self.application.close()


#     def test_users_json_is_not_empty(self):
#         self.assertNotEqual(path.getsize("src/db/users.json"), 0)
