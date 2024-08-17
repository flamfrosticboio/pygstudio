# Pygstudio

A template to make games easier like what you see in game engines like Unity and Roblox.

## How to use pygstudio
- To create your own pygstudio project, type in your terminal:
`pygstudio create [NAME]` or `python -m pygstudio create [NAME] -o [DESTINATION]`.
This will make a new pygstudio template in your directory / destination.

## What can you do with pygstudio?
1. Easy configuration - Each file are provided with comments to help you guide in building your game. You can also edit the code if you don't like the code.
2. Easy access - Your scripts can access various things like the globals, components and assets by putting these lines of code: `import globals` `import components` `pygame.image.load("assets/mypicture.png")` (an example of using assets). Example:
``` python
# scripts/npc.py
import pygame, random, globals
from components import characters

for i in range(10):
    npc_character_image = pygame.image.load("assets/smol_npc.png")
    new_npc = components.characters.NPC(npc_character_image, (random.random() * 100, random.random() * 1000))   # NPC(image, position)
    globals.npcs.append(new_npc)
    new_npc.start_being_npc()
```
3. Threaded scripts - Make a script easily by making a file/package inside the `scripts` directory. 

Instead of this monstrosity:
``` python
import threading

def fire_function_every_3_seconds(): ...   # takes 15 lines of code
def handle_physics(): ...   # takes 300 lines of code 
def handle_network(): ...   # takes 258 lines of code

threading.Thread(daemon=True, target=fire_function_every_3_seconds).start()
threading.Thread(daemon=True, target=handle_physics).start()
threading.Thread(daemon=True, target=handle_network).start()
```
You can now put them in their separate files and they will be executed independently.
``` python
# scripts/loop.py
...     # the entire `fire_function_every_3_seconds` code
```
``` python
# scripts/physics.py
...     # the entire `handle_physics` code
```
``` python
# scripts/network.py
...     # the entire `handle_network` code
```

## Template
The file structure of pygstudio follows (where `NAME` is your project name): 

_(Version 1.0)_
```
[NAME]/
- [NAME].py
- globals.py
- engine.py
- script_manager.py
- assets/
- scripts/
- components/
    - __init__.py
```

## About
Hello, I am only a developer making this project. If you wish to improve this project, you may fork this repository and add me in the credits of your repository. I will still continue improving this project but I cannot guarantee that I can repond to all your issues as I am only a student in a university. Life is hard!

This project is licensed.