class Score:
    """A Class """

    def __init__(self):
        self.score = 0

    def change_Score(self, step=403):
        self.score += step

    def get_Score(self):
        return f"{self.score:05d}"