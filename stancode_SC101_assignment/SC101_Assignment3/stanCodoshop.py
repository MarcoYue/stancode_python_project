"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: Let the annoying people disappear from the background
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r_total = 0
    g_total = 0
    b_total = 0
    points = 0
    for pixel in pixels:
        r_total = r_total + pixel.red
        g_total = g_total + pixel.green
        b_total = b_total + pixel.blue
        points += 1
    r_avg = r_total // points
    g_avg = g_total // points
    b_avg = b_total // points
    avg_list = [r_avg, g_avg, b_avg]
    return avg_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best_pixel = pixels[0]
    shortest_dis = float('inf')  # shortest distance will decrease from infinity.
    avg_rgb = get_average(pixels)
    for pixel in pixels:
        current_dis = get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2])  # current pixel's distance.
        if current_dis < shortest_dis:  # if current pixel distance shorter than shortest, replace the best pixel.
            shortest_dis = current_dis
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    """  
    # for checking milestone 1~3!

    green_im = SimpleImage.blank(20, 20, 'green')
    green_pixel = green_im.get_pixel(0, 0)
    print(get_pixel_dist(green_pixel, 5, 255, 10))

    green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    print(best1.red, best1.green, best1.blue)
    """
    for x in range(width):  # Individually execute for each point.
        for y in range(height):
            compare_pixel = []  # to store the pixel needed to be compared.
            result_pixel = result.get_pixel(x, y)  # get the result pixel
            for image in images:  # for every image in images.
                image_pixel = image.get_pixel(x, y)  # get the current image's pixel.
                compare_pixel += [image_pixel]  # store each image's pixel in current x and y.
            replace_pixel = get_best_pixel(compare_pixel)  # return the best pixel.
            result_pixel.red = replace_pixel.red  # replace pixel
            result_pixel.green = replace_pixel.green
            result_pixel.blue = replace_pixel.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
