class Exercise:
    """Class to handle exercise texts and images.

    Text and image files are named with index numbers, which identify them as part of the same exercise.

    Attributes:
        number: exercise index number integer which is common to text and image file
    """

    def __init__(self, number):
        """Class constructor to create an exercise.

        Args:
            number: exercise index number integer which is common to text and image file
        """
        self.number = number
        self.text = None
        self.image = None

    def get_exercise_text(self):
        """Get exercise text file from exercises folder.

        Returns:
            Exercise description text
        """
        textfile = f'src/exercises/{self.number}.txt'
        with open(textfile, "r") as file:
            text = file.read()
            return text

    def get_exercise_image(self):
        """Get exercise image file from exercises folder.

        Returns:
            Image related to an exercise
        """
        imagefile = f'src/exercises/{self.number}.png'
        with open(imagefile, "r") as file:
            image = file.read()
            return image
