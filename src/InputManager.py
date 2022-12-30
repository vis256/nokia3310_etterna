import RPi.GPIO as GPIO

keys = {
    'left': 26,
    'down': 19,
    'up': 13,
    'right': 6
}

class InputManager:
    def __init__(self):
        self.held = {}

        for k, v in keys.items():
            GPIO.setup(v, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            self.held[k] = False

    def isPressed(self, key):
        inpt = not GPIO.input(keys[key])
        if inpt == True:
            if not self.held[key]:
                self.held[key] = True
                return True
            else:
                return False
        else:
            self.held[key] = False
            

    def pressed(self):
        pressed = []
        
        for k, _ in keys.items():
            res = self.isPressed(k)
            if res == True:
                pressed.append(k)

        return pressed
