import unittest
from exercise import Exercise


class TestExercise(unittest.TestCase):
    def setUp(self):
        self.exercise = Exercise("1")

    def test_exercise_text_correct(self):
        self.assertEqual(self.exercise.get_exercise_text(),
                         "Look away from the screen, into the distance. \n")
