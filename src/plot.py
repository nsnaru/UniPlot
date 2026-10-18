##
# An experimental text-based function plotter.
##

import math

print("UniPlot by N. Naru")

name = input("Plot file name: ") + '.txt'

w = int(input("Width: "))
h = int(input("Height: "))

x_scale = float(input("X full scale: ")) / w
y_scale = float(input("Y full scale: ")) / h

boldness = float(input("Boldness: "))

# Create a 2D array with dimensions w by h.
points = [[0 for x in range(h)] for y in range(w)]

# Light to heavy
#thresholds = [1.25, 1, 0.8, 0.5]
thresholds = [2, 1.5, 1, 0.5]


# Light to heavy
shades = ["\u2591", "\u2592", "\u2593", "\u2588"]


# Arbitrary function to plot
def f(x):
    return math.sin(x)

# Assigns the correct shade to each point on the grid depending on its proximity to the true non-quantised value of f(x).
def shader(s):
    shade = 0
    for i in range(len(shades)):
        if s <= thresholds[i] * boldness:
            shade += 1
    return shade

# Plots points where the centre of 'points' (both vertically and horizontally) is considered the origin.
def point(x, y, v):
    points[x + round(w/2)][round(h/2) - y] = v

# Plot the f(x) into the 'points' array.
for x in range(round(-w/2), round(w/2)):
    for y in range(round(-h/2) + 1, round(h/2)):
        proximity = abs(f(x*x_scale)/y_scale - y)
        point(x, y, shader(proximity))

# Render and write plot to file
with open(name, 'w') as f:
    for y in range(h):
        for x in range(w):
            if points[x][y] != 0: f.write(shades[points[x][y]-1])

            elif x == w/2: f.write(":")   # y-axis line
            elif y == h/2: f.write(".")   # x-axis line
            
            else: f.write(" ")
            
        f.write("\n")
