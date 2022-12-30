from luma.core.render import canvas
from demo_opts import get_device
import time
from DrawUtils import drawField

def main():
    cols = device.width
    rows = device.height
    
    while True:
        with canvas(device, dither=True) as draw:
            drawField(draw, cols, rows)
            time.sleep(1)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
