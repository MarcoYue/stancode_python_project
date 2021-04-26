"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
Marco Yue:
There's my breakout here.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 1		# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    lives = NUM_LIVES
    end_game = False
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while True:
        pause(FRAME_RATE)
        if graphics.activate is True:  # if player mouseclick, start game.
            graphics.first_ball.move(dx, dy)
            if graphics.first_ball.x <= 0 or graphics.first_ball.x+graphics.first_ball.width > graphics.window.width:
                dx = -dx
            if graphics.first_ball.y <= 0:
                dy *= -1
                graphics.verse_y()  # because the wall reflect event didn't return to class. I have to manually edit it.
            if graphics.conflict() is True:  # if there is a conflict
                graphics.crash()  # to judge is paddle or brick. if it's a brick, crush it!
                graphics.reflect()  # to reflect
                dy = graphics.get_dy()  # new dy
            if graphics.win_game_judge():  # to judge if player wins.
                print('WIN GAME!')
                graphics.activate = False
                graphics.reset_ball()
                graphics.win_game_label()
                break
            if graphics.ball_go_down():  # if the ball fall, lives is decreased.
                lives = lives - 1
                if lives > 0:
                    graphics.reset_ball()
                    dx = graphics.get_dx()
                    graphics.activate = False  # stop the game, player need to click mouse to keep playing.
                else:  # player just lose the game
                    graphics.end_game_symbol()
                    graphics.activate = False
                    graphics.reset_ball()
                    break


# def explode(graphics_e):
#     if graphics_e.explode_1.x > -graphics_e.explode_1.width or graphics_e.explode_1.y > 0:
#         graphics_e.explode_1.move(-10, -10)
#     if graphics_e.explode_2.x < graphics_e.window.width or graphics_e.explode_2.y > 0:
#         graphics_e.explode_2.move(10, -10)
#     if graphics_e.explode_3.x > -graphics_e.explode_3.width or graphics_e.explode_3.y > graphics_e.window.height:
#         graphics_e.explode_3.move(-10, 10)
#     if graphics_e.explode_4.x < graphics_e.window.width or graphics_e.explode_4.y < graphics_e.window.height:
#         graphics_e.explode_4.move(10, 10)



if __name__ == '__main__':
    main()