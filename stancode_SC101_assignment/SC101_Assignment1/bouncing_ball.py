"""
File: bouncing_ball.py
Name: Marco Yue
-------------------------
TODO: bouncing a ball three times then stop
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window = GWindow(800, 500, title='bouncing_ball.py')
play_time = 0  # counts the playtime
activate = False  # a toggle to control status


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    window.add(ball)
    onmouseclicked(ball_bounce)

    pass


def ball_bounce(mouse):
    global START_X, START_Y, play_time, activate

    if play_time == 3:  # end process
        activate = True
    if not activate:
        vy = GRAVITY
        activate = True  # if start playing, switch to True to prevent mouseclick disturb
        while True:
            if ball.x-SIZE/2 >= window.width:
                activate = False  # out of x range, reset status
                play_time += 1
                break
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + SIZE/2 >= window.height:
                vy = vy * -REDUCE
            pause(DELAY)
        window.add(ball, START_X, START_Y)  # add a ball for every new start.


if __name__ == "__main__":
    main()
