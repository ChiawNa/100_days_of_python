import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('C:\\Users\ASUS\OneDrive\\100 days of python\\Day_18 - Turtle & Graphical User Interface (GUI)\\hirst_painting_dot.jpg', 32)

# Create a list of tuples containing the RGB values
color_tuples = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    color_tuples.append(new_color)

# Print the list of color tuples
print(color_tuples)

color_list = [(84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]