import Timer
import Ruleset
from Note import Note
from DrawUtils import drawArrow
import random

class Lane:
    def __init__(self, scrollDirection, scrollSpeed, judgementHeight, noteSymbol, laneHeight, laneX):
        self.scrollDirection = scrollDirection
        self.scrollSpeed = scrollSpeed
        self.judgementHeight = judgementHeight

        self.noteSymbol = noteSymbol

        self.laneHeight = laneHeight
        self.laneX = laneX


        self.notes = [int(5000 + 6000 * random.random() * i) for i in range( 1, 200 )]
    
        self.notes.sort()
        self.notes = [Note(x) for x in self.notes]

        # https://osu.ppy.sh/community/forums/topics/976158?n=1
        self.maxTimeVisible = 13720 / scrollSpeed

        self.visibleNotes = [None for _ in range(self.laneHeight)]    

        self.ratings = self.buildRating()

    def setNotes(self, notes):
        self.notes = notes

    def tick(self):
        t = Timer.GLOBAL_TIMER.getTime()

        missed = False

        self.visibleNotes = [None for _ in range(self.laneHeight)]    
        
        for note in self.notes:
            np = self.getNotePos(note.time, t)
            if np is not None:
                if np < len(self.visibleNotes):
                    self.visibleNotes[np] = note
            else:
                missed = True
                self.notes.remove(note)

        return missed

    def getCorrectY(self, y):
        return y if self.scrollDirection == 'up' else self.laneHeight - y 

    def getNotePos(self, noteTime, timerTime):
        t = noteTime - timerTime
        if t < 0:
            return None

        return int((t / self.maxTimeVisible) * self.laneHeight) 
        
    def print(self):
        for index, note in enumerate(self.visibleNotes):
            if note is not None:
                print(self.noteSymbol, end="")
            elif index == self.judgementHeight:
                print("|", end="")
            else:
              print(" ", end="")  
        print("")


    def draw(self, draw):
        drawArrow(draw, self.laneX, self.getCorrectY( self.judgementHeight ), self.noteSymbol)
        for index, note in enumerate(self.visibleNotes):
            if note is not None:
                drawArrow(draw, self.laneX, self.getCorrectY(index), self.noteSymbol)
        

    def buildRating(self):
        ratings = {}
        ratings[self.judgementHeight] = 'Max'
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
                    self.notes.remove(note)
                    self.visibleNotes[index] = None
                    return input_result
                return None
        return None



