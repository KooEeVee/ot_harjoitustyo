# import unittest
# from database import Database
# from config import DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME

# class TestDatabase(unittest.TestCase):
#     def setUp(self):
#         self.db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME)

#     def test_database_connect(self):
#         self.db.connect_db()
#         self.assertNotEqual(self.db.get_rows(), 0)

#     def test_database_disconnect(self):
#         self.db.disconnect_db()
#         self.db.get_rows()
#         self.assertRaises(Exception)
