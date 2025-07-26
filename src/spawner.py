import random
from config import LANES, SCREEN_HEIGHT
from src.car import Car

def spawn_enemy_car():
    lane_x = random.choice(LANES)
    speed = random.randint(4, 7)
    image_path = random.choice([
        "assets/cars/enemy1.png",
        "assets/cars/enemy2.png"
    ])
    return Car(image_path, lane_x, -100, speed)
