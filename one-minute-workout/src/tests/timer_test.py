import unittest
from timer import Timer
from user import User


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.user = User("timertest", "1234")
        self.timer = Timer("20:20", "30", "timertest")

    def test_timer_data_saved_to_user(self):
        self.user.new_user_json()
        self.timer.save_timer_to_user()
        self.assertEqual(self.timer.get_timer_from_user(),
                         "End time: 20:20, Interval: 30")

    def test_timer_stop_is_correct_in_json(self):
        self.assertEqual(self.user.get_timer_stop(),
                         "20:20")

    def test_timer_interval_is_correct_in_json(self):
        self.assertEqual(self.user.get_timer_interval(),
                         "30")
