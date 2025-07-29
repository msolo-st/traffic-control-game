import random
from config import LANES, SCREEN_HEIGHT
from src.car import Car

def spawn_enemy_car():
    lane_x = random.choice(LANES)
    speed = random.randint(4, 7)
    image_path = random.choice([
        "assets/images/enemy1.png",
        "assets/images/enemy2.png"
    ])
    return Car(image_path, lane_x, -100, speed)
