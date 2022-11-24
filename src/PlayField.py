from Lane import Lane

class PlayField:
    def __init__(self):
        self.Lanes = [Lane('up', 10, 3, 'X') for _ in range(4)]

    def tick(self):
        for lane in self.Lanes:
            lane.tick()

    def getLane(self, index):
        return self.Lanes[index]

    def print(self):
        for lane in self.Lanes:
            lane.print()
    
