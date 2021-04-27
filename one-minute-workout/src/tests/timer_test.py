import unittest
from timer import Timer


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = Timer("10:10", "20:20", "30", "testname")

    def test_timer_data_saved_to_user(self):
        self.timer.save_timer_to_user()
        self.assertEqual(self.timer.get_timer_from_user(),
                         "Start time: 10:10, End time: 20:20, Interval: 30")
