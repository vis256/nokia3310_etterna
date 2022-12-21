import Timer
import Ruleset
from Note import Note

LANE_PIXEL_HEIGHT = 80

class Lane:
    def __init__(self, scrollDirection, scrollSpeed, judgementHeight, noteSymbol):
        self.scrollDirection = scrollDirection
        self.scrollSpeed = scrollSpeed
        self.judgementHeight = judgementHeight

        self.noteSymbol = noteSymbol
        
        self.notes = [
            Note(1000),
            Note(2000),
            Note(3000),
            Note(4000),
            Note(5000),
            Note(6000),
            Note(7000),
        ]
        # https://osu.ppy.sh/community/forums/topics/976158?n=1
        self.maxTimeVisible = 13720 / scrollSpeed

        self.visibleNotes = [None for _ in range(LANE_PIXEL_HEIGHT)]    

        self.ratings = self.buildRating()

        print(self.ratings)
    def setNotes(self, notes):
        self.notes = notes

    def tick(self):
        t = Timer.GLOBAL_TIMER.getTime()
        self.visibleNotes = [None for _ in range(LANE_PIXEL_HEIGHT)]    
        
        for note in self.notes:
            np = self.getNotePos(note.time, t)
            if np is not None and np < len(self.visibleNotes):
                self.visibleNotes[np] = note

    def getNotePos(self, noteTime, timerTime):
        t = noteTime - timerTime
        if t < 0:
            return None

        return int((t / self.maxTimeVisible) * LANE_PIXEL_HEIGHT) 
        
    def print(self):
        for index, note in enumerate(self.visibleNotes):
            if note is not None:
                print(self.noteSymbol, end="")
            elif index == self.judgementHeight:
                print("|", end="")
            else:
              print(" ", end="")  
        print("")

    def buildRating(self):
        ratings = {}
        ratings[self.judgementHeight] = 'Perfect'
        for rating in Ruleset.GLOBAL_RULESET.keys():
            for i in range(Ruleset.GLOBAL_RULESET[rating] ):
                ratings[self.judgementHeight - i] = rating
                ratings[self.judgementHeight + i] = rating
        return ratings

    def input(self):
        for index, note in enumerate(self.visibleNotes):
            if note is not None:
                if index in self.ratings:
                    input_result = self.ratings[index]
                    self.visibleNotes[index] = None
                    return input_result
        return None

            
