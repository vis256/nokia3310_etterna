def drawArrow(draw, x, y, direction):
    if direction == 'left':
        draw.polygon([(x, y-2), (x-2, y), (x, y+2), (x,y), (x+2, y), (x,y)])
    elif direction == 'down':
        draw.polygon([(x, y-2), (x,y), (x-2, y), (x, y+2), (x+2, y), (x,y)])
    elif direction == 'up':
        draw.polygon([(x, y+2), (x,y), (x+2, y), (x, y-2), (x-2, y), (x,y)])
    elif direction == 'right':
        draw.polygon([(x-2, y), (x,y), (x, y-2), (x+2, y), (x, y+2), (x,y)])


def drawField(draw, cols, rows):
    draw.line((5, 0, 5, rows), fill="white")
    draw.line((33, 0, 33, rows), fill="white")


def drawScore(draw, label, score, y, cols):
    text = f"{label}: {score}"
    size = draw.textsize(text)
    x = cols - 2 - size[0]

    draw.text((x, y), text, fill="white")

def drawCombo(draw, comboScore, y, xleft, xright):
    text = f"{comboScore}x"

    mx = (xright - xleft) // 2

    draw.text((mx, y), text, fill="white")
