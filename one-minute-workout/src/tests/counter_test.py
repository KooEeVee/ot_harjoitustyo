import unittest
from datetime import datetime
from counter import Counter


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter_today = Counter("11:00", "10")
        self.counter_tomorrow = Counter("09:00", "60")

    def test_correct_loop_count_same_day(self):
        self.counter_today.now = datetime(2021, 12, 24, 10, 1)
        self.assertEqual(self.counter_today.count_exercise_loops(),
                         (5.0, 600))

    def test_correct_loop_count_day_after(self):
        self.counter_tomorrow.now = datetime(2021, 12, 24, 10, 00)
        self.assertEqual(self.counter_tomorrow.count_exercise_loops(),
                         (23.0, 3600))
