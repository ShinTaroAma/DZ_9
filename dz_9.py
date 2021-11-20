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

def move():
    for b in bullets:
        b["y"] -= BULLET_SPEED
        if  b["y"] < 1:
            for brick in bricks:
                if b["x"] == brick ["x"]:
                    brick["val"] -= 1
                    if brick["val"] == 0:
                        bricks.remove(brick)
            bullets.remove(b)

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


def press_instruction(key):
    global ship
    if key == pynput.keyboard.Key.right:
        if ship["x"] < WIDTH - 1:
            ship["x"] += 1
        
    elif key == pynput.keyboard.Key.left:
        if ship["x"] > 0:
            ship["x"] -= 1
    elif key == pynput.keyboard.Key.space:
        bullets.append({"x": ship["x"], "y": HEIGHT - 1})

pynput.keyboard.Listener(on_press = press_instruction).start()

while(True):
    os.system('cls')
    draw()
    move()
    time.sleep(0.1)

