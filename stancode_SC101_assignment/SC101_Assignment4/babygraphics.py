"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    gap = (width-2*GRAPH_MARGIN_SIZE)//len(YEARS)  # calculate x axis gap
    x = GRAPH_MARGIN_SIZE+gap*year_index
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    for y_index in range(len(YEARS)):  # draw some default line.
        x_pos = get_x_coordinate(CANVAS_WIDTH, y_index)
        canvas.create_line(x_pos, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE/2, x_pos, GRAPH_MARGIN_SIZE/2, width=LINE_WIDTH, fill='black')
        canvas.create_text(x_pos+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+TEXT_DX, text=YEARS[y_index], anchor=tkinter.NW, font='times 15')
    #################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    rank_distance = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2) / 1000  # Let Y axis be divided into 1000 equal parts.
    gap = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)  # X axis gap
    # Write your code below this line
    for n_index in range(len(lookup_names)):  # do each search name
        rank = []
        for y_index in range(len(YEARS)):  # do each year (from 1900 to 2010)
            if str(YEARS[y_index]) in name_data[lookup_names[n_index]]:  # if 'current name' exists 'current year'
                rank.append(name_data[lookup_names[n_index]][str(YEARS[y_index])])  # add it to rank list
            else:
                rank.append('*')  # means its rank is over 1000.
        x_pos_2 = 0
        y_pos_2 = 0
        word_2 = ''
        color_index = n_index % len(COLORS)  # color_index will be 0,1,2,3

        for i in range(len(YEARS)-1):  # draw line and text
            if rank[i] == '*':  # the y position of the line's first point
                y_pos = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y_pos = GRAPH_MARGIN_SIZE + rank_distance * int(rank[i])
            if rank[i+1] == '*':  # the y position of the line's second point
                y_pos_2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y_pos_2 = GRAPH_MARGIN_SIZE + rank_distance * int(rank[i+1])
            x_pos = GRAPH_MARGIN_SIZE + gap*i  # the x position of the line's first point
            x_pos_2 = GRAPH_MARGIN_SIZE + gap*(i+1)  # the x position of the line's second point
            canvas.create_line(x_pos, y_pos, x_pos_2, y_pos_2, width=LINE_WIDTH, fill=COLORS[color_index])
            word = lookup_names[n_index] + ' ' + rank[i]  # text word
            word_2 = lookup_names[n_index] + ' ' + rank[i+1]
            canvas.create_text(x_pos+TEXT_DX, y_pos-TEXT_DX, text=word, anchor=tkinter.SW, font='times 12', fill=COLORS[color_index])

        # the line at 119 is to draw the last text, and to avoid obob issue. I think I have a bad writing style here.
        # variable in line 96,97,98 is also to avoid obob issue, i think its quite stupid.
        canvas.create_text(x_pos_2 + TEXT_DX, y_pos_2 - TEXT_DX, text=word_2, anchor=tkinter.SW, font='times 12', fill=COLORS[color_index])
    #################################


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
