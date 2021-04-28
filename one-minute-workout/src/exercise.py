class Exercise:
    def __init__(self, number):
        self.number = number
        self.text = None
        self.image = None

    def get_exercise_text(self):
        textfile = f'src/exercises/{self.number}.txt'
        with open(textfile, "r") as f:
            text = f.read()
            return text
            
    def get_exercise_image(self):
        imagefile = f'src/exercises/{self.number}.png'
        with open(imagefile, "r") as f:
            image = f.read()
            return image
