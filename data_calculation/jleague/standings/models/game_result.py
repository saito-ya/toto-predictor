class GameResult:
    class_name = None

    def __init__(self):
        self.class_name = 'GameResult'

    def get_classname(self) -> str:
        return self.class_name