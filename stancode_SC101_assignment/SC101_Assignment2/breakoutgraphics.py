"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE

Marco Yue:
I'm not sure it's ok or not, I'm just wondering there's a bug somewhere that i just can't figure it out.
I think I had a bad writing style and programing structure here.
but anyway it finally works!

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 5        # Number of rows of bricks.
BRICK_COLS = 5       # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 100      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 5  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle_offset = PADDLE_OFFSET
        self.ball_r = BALL_RADIUS
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'blue'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.first_ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.first_ball.filled = True
        self.first_ball.fill_color = 'black'
        self.window.add(self.first_ball)
        self.initial_x = (window_width-ball_radius)/2
        self.initial_y = (window_height-ball_radius)/2
        # Default initial velocity for the ball

        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self.activate = False
        self.crash_is_paddle = False
        self.point_count = 0
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_start)

        # Draw bricks

        for y_pos in range(0, (BRICK_HEIGHT+BRICK_SPACING)*BRICK_ROWS-BRICK_SPACING, BRICK_HEIGHT+BRICK_SPACING):
            for x_pos in range(0, (BRICK_WIDTH+BRICK_SPACING)*BRICK_COLS-BRICK_SPACING, BRICK_WIDTH+BRICK_SPACING):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if y_pos < BRICK_HEIGHT+BRICK_SPACING * 2 + 1:
                    self.brick.fill_color = 'red'
                elif y_pos < (BRICK_HEIGHT+BRICK_SPACING) * 4:
                    self.brick.fill_color = 'orange'
                elif y_pos < (BRICK_HEIGHT+BRICK_SPACING) * 6:
                    self.brick.fill_color = 'yellow'
                elif y_pos < (BRICK_HEIGHT+BRICK_SPACING) * 8:
                    self.brick.fill_color = 'green'
                elif y_pos < (BRICK_HEIGHT+BRICK_SPACING) * 10:
                    self.brick.fill_color = 'blue'
                else:
                    self.brick.fill_color = 'black'
                self.window.add(self.brick, x=x_pos, y=y_pos)

    def paddle_move(self, paddle_mouse):  # let the paddle move.
        if paddle_mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif paddle_mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = paddle_mouse.x - self.paddle.width/2
        pass

    def ball_start(self, game_start_mouse):  # player click the mouse, game is activated!
        self.activate = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_go_down(self):  # judge if the ball lower than the paddle.
        if self.first_ball.y > self.paddle.y + self.paddle.width/2:
            return True

    def reset_ball(self):  # reset the ball position and give it a new dx and dy.
        self.first_ball.x = self.initial_x
        self.first_ball.y = self.initial_y
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.activate = False

    def conflict(self):  # deal with collision
        self.left_top = self.window.get_object_at(self.first_ball.x, self.first_ball.y)
        self.right_top = self.window.get_object_at(self.first_ball.x+2*BALL_RADIUS, self.first_ball.y)
        self.left_down = self.window.get_object_at(self.first_ball.x, self.first_ball.y+2*BALL_RADIUS)
        self.right_down = self.window.get_object_at(self.first_ball.x+2*BALL_RADIUS, self.first_ball.y+2*BALL_RADIUS)
        if self.left_top is None and self.right_top is None and self.left_down is None and self.right_down is None:
            return False  # means there's no collision.
        else:
            return True  # means there's a collision

    def crash(self):  # if the conflict object is brick, remove it, if is not, return crash_is_paddle status to 'True'.
        if self.left_top is not self.paddle and self.left_down is not self.paddle and self.right_top is not self.paddle and self.right_down is not self.paddle:
            self.window.remove(self.left_top)
            self.window.remove(self.right_top)
            self.window.remove(self.left_down)
            self.window.remove(self.right_down)
            self.point_count += 1
            self.crash_is_paddle = False
        else:
            self.crash_is_paddle = True

    def reflect(self):  # reflect the ball
        if self.crash_is_paddle is True:  # ball collide with paddle.
            if self.first_ball.y+2*BALL_RADIUS >= self.window.height - self.paddle.height - self.paddle_offset + INITIAL_Y_SPEED:
                pass  # need to notice that ball.y position need to higher than the paddle, or it will cause some bug.
            else:
                self.__dy *= -1
        else:
            self.__dy *= -1

    def end_game_symbol(self):  # show the end game symbol
        self.lose_label = GLabel('YOU DIE', x=self.window.width*0.4, y=self.window.height/2)
        self.lose_label.font = 'Courier-13'
        self.lose_label.color = 'red'
        self.window.add(self.lose_label)

    def win_game_label(self):  # show that player win game.
        self.win_label = GLabel('VICTORY', x=self.window.width*0.4, y=(self.window.height-BALL_RADIUS)/2)
        self.win_label.font = 'Courier-13'
        self.win_label.color = 'limegreen'
        self.window.add(self.win_label)

    def win_game_judge(self):  # to confirm that player just win the game.
        for y_pos in range(0, (BRICK_HEIGHT+BRICK_SPACING)*BRICK_ROWS-BRICK_SPACING, BRICK_HEIGHT+BRICK_SPACING):
            for x_pos in range(0, (BRICK_WIDTH+BRICK_SPACING)*BRICK_COLS-BRICK_SPACING, BRICK_WIDTH+BRICK_SPACING):
                obj = self.window.get_object_at(x_pos+1, y_pos+1)
                if obj is not None and obj is not self.first_ball and obj is not self.paddle:
                    return False
        return True

    def verse_y(self):  # some disgusting method to let me avoid bug....
        self.__dy *= -1
