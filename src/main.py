from GameState import GameState
import Timer

def main():
    Game = GameState()    

    while True:
        Game.tick()
        Game.print()
        Timer.GLOBAL_TIMER.tick()
        
if __name__ == "__main__":
    main()
