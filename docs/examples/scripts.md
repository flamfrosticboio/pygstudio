# Pygstudio Example: Scripts - Jumper
A source code that makes a simple jumping game using a feature `scripts`.
> Recommend reading the example overview. 

### Step 1: **Make a pygstudio project using pygstudio.**
Using your terminal, create a new pygstudio project using `python -m pygstudio create [NAME]` (for my example: `python -m pygstudio create jumper`)

### Step 2: **Coding the game**
1. Navigate to your project
2. In the scripts directory in your project, create a new file called `physics.py`. This will be your physics simulation script for your player.
3. In the components directory in your project, create a new file called `player.py`. This will store the player class.

Now you should have a project directory like this (where `NAME` is your project name):
```
[NAME]/
├── assets/
├── components/
│   ├── __init__.py
│   └── player.py
├── scripts/
│   └── physics.py
├── globals.py
├── script_manager.py
├── [NAME].py
└── engine.py
```

4. In our `globals.py`:

Add these lines of code under the variable `screen`. This is our global variables that is accessible to our scripts. 
``` python
from components.player import Player, Block
player = Player((200, 50))
mvmap = [False, False, False]
blocks = [
    Block((10, 400), (200, 10)),
    Block((450, 400), (200, 10)),
    Block((200, 375), (250, 10))
]

PLAYER_SPEED = 3
PLAYER_JUMPPOWER = 5
AIRTIME_THRESHOLD = 3
FRICTION = 0.8
GRAVITY = 20

player_vel_x = 0
player_vel_y = 0 
air_time = 0
```

In our bindable function `on_event(event: pygame.event.Event)`, add these lines of code. This will keep track of our keypresses
``` python
global player_vel_x, player_vel_y
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP: mvmap[0] = True
    elif event.key == pygame.K_LEFT: mvmap[1] = True
    elif event.key == pygame.K_RIGHT: mvmap[2] = True
elif event.type == pygame.KEYUP:
    if event.key == pygame.K_UP: mvmap[0] = False
    elif event.key == pygame.K_LEFT: mvmap[1] = False
    elif event.key == pygame.K_RIGHT: mvmap[2] = False
```

Lastly, in our bindable function `on_render(surface: pygame.Surface)`, add these lines of code to render our blocks and player.
``` python
for block in blocks: block.render(screen)
player.render(screen)
```
> Tip: Coding is not following the format everyone uses but to at least make it readable to others.

5. In our `components/player.py`, we add these lines of code to define our player and block.
``` python
import pygame as pg

class Player:
    def __init__(self, pos) -> None:
        self.image = pg.Surface((20, 20))
        self.rect = pg.Rect(pos, (20, 20))
        
    def render(self, surface):
        surface.blit(self.image, self.rect)
        
class Block:
    def __init__(self, pos, size):
        self.image = pg.Surface(size)
        self.rect = pg.Rect(pos, size)
        
    def render(self, surface):
        surface.blit(self.image, self.rect)
```

6. In our `scripts/physics.py`, we add these lines of code to make the player have physics.
``` python
from time import time, sleep
import globals
# it is also possible to do `from globals import *`

fps = 1/60
last_dt = 0

while globals.running:
    # A good game developer always use delta time for physics and animation (dt)
    dt = time() - last_dt
    
    if globals.mvmap[0] and globals.air_time <= globals.AIRTIME_THRESHOLD: 
        globals.player_vel_y = -globals.PLAYER_JUMPPOWER
    
    if globals.mvmap[1] and globals.mvmap[2]: pass
    elif globals.mvmap[1]: globals.player_vel_x = -globals.PLAYER_SPEED
    elif globals.mvmap[2]: globals.player_vel_x = globals.PLAYER_SPEED
    
    globals.player_vel_y += (globals.GRAVITY * fps)
    globals.player.rect.y += int(globals.player_vel_y)
    globals.air_time += 1
    
    # Checking collision at y level
    for block in globals.blocks:
        collided = globals.player.rect.colliderect(block.rect)
        if collided:
            globals.player_vel_y = 0
            globals.air_time = 0
            globals.player.rect.bottom = block.rect.top
            
    globals.player.rect.x += int(globals.player_vel_x)
    globals.player_vel_x *= globals.FRICTION
    
    # Checking collision at x level
    for block in globals.blocks:
        collided = globals.player.rect.colliderect(block.rect)
        if collided:
            if globals.player_vel_x > 0:
                globals.player.rect.right = block.rect.left
            elif globals.player_vel_x < 0:
                globals.player.rect.left = block.rect.right
            globals.player_vel_x = 0
    
    last_dt = time()
    sleep(fps)
```

### Step 3: Run the game
From your terminal, type `python [NAME].py` (where `NAME` is your project name) to run the game.