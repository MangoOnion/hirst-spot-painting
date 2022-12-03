import colorgram
from turtle import Turtle, Screen, colormode
import random
colours = colorgram.extract('image.jpg', 1000)

colour_list = []
for i in range(len(colours)):
    next_color = colours[i]
    rgb = next_color.rgb
    colour = (rgb[0], rgb[1], rgb[2])
    colour_list.append(colour)
    i += 1

# colour_list = [(237, 233, 221), (134, 90, 53), (200, 154, 115), (57, 30, 20), (59, 99, 118), (23, 44, 68), (129, 72, 85), (71, 107, 84), (69, 27, 36), (227, 238, 230), (121, 31, 41), (130, 33, 24), (174, 145, 50), (22, 51, 36), (186, 100, 85), (140, 168, 153), (79, 83, 25), (226, 202, 126), (132, 157, 166), (21, 90, 57), (181, 140, 149), (231, 172, 161), (166, 102, 114), (220, 231, 236), (8, 89, 108), (38, 60, 97), (239, 222, 226), (93, 148, 130), (90, 145, 152), (224, 171, 181), (171, 203, 189), (119, 126, 140), (164, 204, 210), (184, 190, 202)]
# print(len(colour_list))

draw = Turtle()
ypos = -225
colormode(255)
colour_num = 0
draw.speed("fastest")
draw.penup()

def draw_ten():
    for _ in range(10):
        dot_colour = random.choice(colour_list)
        draw.color(dot_colour)
        draw.dot(20)
        draw.forward(50)


for _ in range(10):
    draw.goto(-225, ypos)
    draw_ten()
    ypos += 50

draw.setheading(180)
draw.forward(50)

screen = Screen()
screen.screensize(50, 50)
screen.exitonclick()