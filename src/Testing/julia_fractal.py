#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time


def getColorFromPalette(z):
    """Return the index of the color of the current pixel within the Julia set
    in the palette array"""

    # c is the Julia Constant; varying this value can yield interesting images
    julia_constant = complex(-1.0, 0.0)

    for i in range(len(grad)):
        z = z * z + julia_constant  # Iteratively compute z1, z2, z3 ...
        if abs(z) > 2:
            return grad[i]  # The sequence is unbounded
    return grad[-1]         # Else this is a bounded sequence

def getNumber(z):
    """Used for testing. Gets number of iterations rather than color"""

    # c is the Julia Constant; varying this value can yield interesting images
    julia_constant = complex(-1.0, 0.0)

    for i in range(len(grad)):
        z = z * z + julia_constant  # Iteratively compute z1, z2, z3 ...
        if abs(z) > 2:
            return i  # The sequence is unbounded
    return len(grad)         # Else this is a bounded sequence

def makePicture(f, win, photo):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 512x512 pixels."""

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))

    # Display the image on the screen
    canvas = Canvas(win, width=512, height=512, bg="#FFFFFF")
    canvas.pack()
    canvas.create_image((256, 256), image=photo, state="normal")

    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    size = abs(max[0] - min[0]) / 512.0

    canvas.pack()
    for r in range(512, 0, -1):
        for c in range(512):
            x = min[0] + c * size
            y = min[1] + r * size
            c2 = getColorFromPalette(complex(x, y))
            photo.put(c2, (c, 512 - r))
        win.update()  # display a row of pixels


# This is the color palette, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
grad = [
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
]


# This dictionary contains the different views of the Julia set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program?
f = {
        'fulljulia': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0,
            },

        'hourglass': {
            'centerX':     0.618,
            'centerY':     0.00,
            'axisLength':  0.017148277367054,
        },

        'lakes': {
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLength': 0.164938488846612,
            },

        }

def julia_main(i):
    # Set up the GUI so that we can display the fractal image on the screen
    b4 = time()
    win = Tk()

    photo = PhotoImage(width=512, height=512)
    makePicture(f[i], win=win, photo=photo)

    print(f"Done in {time() - b4:.3f} seconds!", file=sys.stderr)
    # Output the Fractal into a .png image
    photo.write(i + ".png")
    print("Wrote picture " + i + ".png")

    print("Close the image window to exit the program")
    # Call tkinter.mainloop so the GUI remains open
    mainloop()


if __name__ == '__main__':
    # Process command-line arguments, allowing the user to select their fractal
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for i in f:
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in f:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in f:
            print(f"\t{i}")
        sys.exit(1)

    # else:
    #     fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])
    #     julia_main(fratcal_config)
