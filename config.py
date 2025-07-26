# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
GRAY  = (128, 128, 128)
YELLOW = (255, 255, 0)

# Player Settings
PLAYER_START_X = SCREEN_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT - 100
PLAYER_SPEED = 5

# Enemy Car Settings
ENEMY_SPEED_MIN = 3
ENEMY_SPEED_MAX = 7
CAR_SPAWN_INTERVAL = 1500  # in milliseconds

# Lane Settings 

LANE_POSITIONS = [150, 300, 450, 600]  # x-coordinates for cars to spawn in

# Scoring 
POINTS_PER_SECOND = 1

# Assets
PLAYER_IMAGE_PATH = "assets/cars/player.png"
ENEMY_IMAGE_PATHS = [
    "assets/cars/enemy1.png",
    "assets/cars/enemy2.png",
    "assets/cars/enemy3.png"
]

# Sound Settings
SOUND_CRASH = "assets/sounds/crash.wav"
SOUND_BG_MUSIC = "assets/sounds/background.mp3"
SOUND_SWITCH = "assets/sounds/switch.wav"
SOUND_HONK = "assets/sounds/honk.wav"
