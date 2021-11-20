import os
import time
import pynput

bullets = [
    {"x": 5, "y": 6},
    {"x": 10, "y": 3}
]
bricks = [
    {"x":10, "val": 9},
 
    {"x":12, "val": 9},
    {"x":14, "val": 9},
    {"x":16, "val": 9}
]


ship = { "x": 5}
HEIGHT = 10
WIDTH = 40
BULLET_SPEED = 0.6



def draw():
    for y in range(HEIGHT):
        result = ""
        for x in range(WIDTH):
            char = " "
            
            for bullet in bullets:
                if x == round(bullet["x"]) and y == round(bullet["y"]):
                    char = "."
            for brick in bricks:
                if y == 0 and x == brick["x"]:
                    char = str(brick["val"])
            if y == 0:
                for b in bricks:
                    if x == b["x"]:
                        char = str(b["val"])
                        
            if x  == ship["x"]  and  y == HEIGHT - 1:
                char = "T"
            result +=char
        print(result)


def def press_instruction(key):
    pass

