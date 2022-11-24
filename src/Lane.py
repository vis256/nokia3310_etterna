import Timer
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

    def setNotes(self, notes):
        self.notes = notes

    def tick(self):
        t = Timer.GLOBAL_TIMER.getTime()
        self.visibleNotes = [None for _ in range(LANE_PIXEL_HEIGHT)]    
        
        for note in self.notes:
            np = self.getNotePos(note.time)
            if np is not None:
                self.visibleNotes[np] = note

    # FIXME
    def getNotePos(self, noteTime):
        t = noteTime - Timer.GLOBAL_TIMER.getTime()
        if t < self.maxTimeVisible:
            return int(t / self.maxTimeVisible) 
        else:
            return None
        
    def print(self):
        for index, note in enumerate(self.visibleNotes):
            if note is not None:
                print(self.noteSymbol, end="")
            elif index == self.judgementHeight:
                print("|", end="")
            else:
              print(" ", end="")  
        print("")
