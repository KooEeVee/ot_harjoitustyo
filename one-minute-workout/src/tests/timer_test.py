import unittest
from timer import Timer
from user import User


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.user = User("timertest", "1234")
        self.timer = Timer("10:10", "20:20", "30", "timertest")

    def test_timer_data_saved_to_user(self):
        self.user.new_user_json()
        self.timer.save_timer_to_user()
        self.assertEqual(self.timer.get_timer_from_user(),
                         "Start time: 10:10, End time: 20:20, Interval: 30")
