# Pygstudio Example: Overview - Simple block
This is the workflow of the entire sample game which you can also follow.
This also provides a overview of what can pygstudio can do.

### Step 1: **Make a pygstudio project using pygstudio.**
1. Open your favorite terminal (cmd/bash/powershell/etc.)
2. Type these in your terminal to create a new pygstudio project (```pygstudio create [NAME] -o [DESTINATION]```)
For this example, I will name it `my small square`

You should have this file structure directory your project to serve as your template: (Name = your project name)
```
[Name]/
- [Name].py
- globals.py
- engine.py
- script_manager.py
- assets/
- components/
- scripts/
```

### Step 2: **Coding the game**
1. Navigate to your project
2. Open `globals.py` your text editor (notepad/vscode/pycharm/etc.) and add this line of codes in `globals.py`

- This code is placed under the `screen` variable in `globals.py`
``` python
from components import game_classes
movement_map = [False, False, False, False]
player = game_classes.Player((0, 0))
```
> Note: You may expect errors with these code but we will get to it later.

- Under the `on_event()` bindable function. Delete the initial code and add these lines of code:

``` python
# At: def on_event(event):

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT: movement_map[0] = True
    if event.key == pygame.K_UP: movement_map[1] = True
    if event.key == pygame.K_DOWN: movement_map[2] = True
    if event.key == pygame.K_RIGHT: movement_map[3] = True
elif event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT: movement_map[0] = False
    if event.key == pygame.K_UP: movement_map[1] = False
    if event.key == pygame.K_DOWN: movement_map[2] = False
    if event.key == pygame.K_RIGHT: movement_map[3] = False
```
- Under the `on_render()` bindable function. Delete the initial code and add these lines of code:

``` python
# At: def on_render(surface):

if movement_map[0]: player.rect.x += -3
if movement_map[1]: player.rect.y += -3
if movement_map[2]: player.rect.y += 3
if movement_map[3]: player.rect.x += 3

screen.blit(player.image, player.rect)
```
3. Go to `components` directory and add a file called `game_classes.py`
> IMPORTANT: After adding a file in the components directory, run `script_manager.py` in your game directory to update the import statements required for your scripts.

4. Open `game_classes.py` and add these code inside of it.
``` python
import pygame

class Player:
    def __init__(self, position):
        self.image = pygame.Surface((20, 20))
        self.rect = pygame.Rect(position, (20, 20))
```
### Step 3: **Run the game**
(For `pygstudio<=1.0.2`) Before running the game, we must update the components import statements by running `script_manager.py` to update the components import statement. To do that, open the terminal in your game directory and type `python script_manager.py`

Run the game by calling `python [NAME].py` where `NAME` is your game name. For my example, it is `my small square` so I will type in `python "my small square.py"` (double quotes `"` for spaces)

Now you should have a working moving block game whenever you press your arrow keys in your keyboard.