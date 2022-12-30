from luma.core.render import canvas
from GameState import GameState
import Timer
from demo_opts import get_device
import RPi.GPIO as GPIO
from InputManager import InputManager

def main():
    device = get_device()

    cols = device.width
    rows = device.height

    Game = GameState(cols, rows)
    IM = InputManager()

    while True:
        Game.tick()

        # Handle input
        left_input = not GPIO.input(26)
        down_input = not GPIO.input(19)
        up_input = not GPIO.input(13)
        right_input = not GPIO.input(6)

        for pressed_key in IM.pressed():
            Game.input(pressed_key)

        with canvas(device, dither=True) as draw:
            Game.draw(draw, cols, rows)
        # Game.print()
        Timer.GLOBAL_TIMER.tick()
        
if __name__ == "__main__":
    main()
