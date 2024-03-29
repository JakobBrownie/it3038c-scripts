from random import choice, randrange
from string import ascii_uppercase
from turtle import *

from freegames import vector

targets = []
letters = []
score = 0


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw():
    """Draw letters."""
    clear()

    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        write(letter, align='center', font=('Consolas', 20, 'normal'))

    update()


def move():
    """Move letters."""
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_uppercase)
        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 5)


def press(key):
    """Press key."""
    global score

    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1

    print('Score:', score)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
for letter in ascii_uppercase:
    onkey(lambda letter=letter: press(letter), letter)
move()
done()