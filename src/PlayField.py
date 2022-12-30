from Lane import Lane
from DrawUtils import drawField


class PlayField:
    def __init__(self, cols, rows):
        self.Lanes = [
            Lane('down', 16, 3, 'left', rows, 10 + 6 * 0),
            Lane('down', 16, 3, 'down', rows, 10 + 6 * 1),
            Lane('down', 16, 3, 'up', rows, 10 + 6 * 2),
            Lane('down', 16, 3, 'right', rows, 10 + 6 * 3),
        ]

    def tick(self):
        misses = 0
        for lane in self.Lanes:
            if lane.tick() == True:
                misses += 1
        return misses

    def getLane(self, index):
        return self.Lanes[index]

    def print(self):
        for lane in self.Lanes:
            lane.print()

    def draw(self, draw, cols, rows):
        drawField(draw, cols, rows)
        for lane in self.Lanes:
            lane.draw(draw)

    def input(self, key):
        for lane in self.Lanes:
            if lane.noteSymbol == key:
                return lane.input()
