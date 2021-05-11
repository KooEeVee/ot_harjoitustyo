class Exercise:
    """Class to handle exercise texts and images.

    Attributes:
        number (int): exercise index number which is common to text and image file
    """
    def __init__(self, number):
        """Class constructor to create new exercise.

        Args:
            number (int): exercise index number which is common to text and image file
        """
        self.number = number
        self.text = None
        self.image = None

    def get_exercise_text(self):
        """Get exercise text file from exercises folder.

        Returns:
            (String): exercise description
        """
        textfile = f'src/exercises/{self.number}.txt'
        with open(textfile, "r") as f:
            text = f.read()
            return text

    def get_exercise_image(self):
        """Get exercise image file from exercises folder.

        Returns:
            (Image): exercise image
        """
        imagefile = f'src/exercises/{self.number}.png'
        with open(imagefile, "r") as f:
            image = f.read()
            return image
