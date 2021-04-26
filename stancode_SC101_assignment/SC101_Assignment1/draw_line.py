"""
File:  draw_line.py
Name: Marco Yue
-------------------------
TODO: To draw a line....
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30
# Global variable
window = GWindow()
click_count = 0  # counts of user click
circle_x = 0  # the x position of circle
circle_y = 0  # the y position of circle


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_hole)
    pass


def create_hole(mouse1):
    global click_count  # using global variable
    global circle_y
    global circle_x

    if click_count % 2 == 0:  # if click count is even, draw a circle
        hole = GOval(SIZE, SIZE, x=mouse1.x-SIZE/2, y=mouse1.y-SIZE/2)
        hole.filled = False
        window.add(hole)
        circle_x = mouse1.x  # to store the circle's position
        circle_y = mouse1.y

    if click_count % 2 == 1:  # if click count is odd, draw a line.
        maybe_none = window.get_object_at(circle_x, circle_y)  # maybe_noe = circle object
        if maybe_none is not None:  # if there's a object, remove it.
            window.remove(maybe_none)
        line = GLine(circle_x, circle_y, mouse1.x, mouse1.y)  # add line.
        window.add(line)

    click_count += 1  # after all of these, add 1 click count.


if __name__ == "__main__":
    main()
