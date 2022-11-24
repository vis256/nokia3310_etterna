from PlayField import PlayField

class GameState:
    def __init__(self):
        self.tickCount = 0
        self.PlayField = PlayField()

    def tick(self):
        self.PlayField.tick()
        # print(f"tick #: {self.tickCount}, time: {TIMER.getTime()}")

    def print(self):
        self.PlayField.print()
        for _ in range(2):
            print("")
