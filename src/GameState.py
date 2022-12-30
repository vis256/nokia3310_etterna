from PlayField import PlayField
import Ruleset
from DrawUtils import drawScore, drawCombo

class GameState:
    def __init__(self, cols, rows):
        self.tickCount = 0
        self.PlayField = PlayField(cols, rows)

        self.score = {}
        for rating in Ruleset.GLOBAL_RULESET.keys():
            self.score[rating] = 0

        self.combo = 0

    def tick(self):
        mc = self.PlayField.tick()
        if mc > 0:
            self.score['Miss'] += mc
            self.combo = 0

    def draw(self, draw, cols, rows):
        self.PlayField.draw(draw, cols, rows)
        y = 0
        for jdgmnt in Ruleset.GLOBAL_RULESET.keys():
            drawScore(draw, jdgmnt, self.score[jdgmnt], y, cols)
            y += 12

        if self.combo > 4:
            drawCombo(draw, self.combo, 20, 5, 33)

    def print(self):
        self.PlayField.print()
        for _ in range(2):
            print("")

    def input(self, key):
        jdgment = self.PlayField.input(key)
        if jdgment is not None:
            self.score[jdgment] += 1
            if jdgment is not 'Miss':
                self.combo += 1
            else:
                self.combo = 0
