## Documentation: Pygstudio Release

`pygstudio release` takes no positional argument.
By default, the arguments passed are: 

* _project folder_ = "."
* _release folder_ = "./release"

### Optional Arguments
* `-f`, `--folder`: the project directory to be release. Example: 'pygstudio release -f "C:/projects/python/my small square"'
* `-o`, `--output`: the output folder for the released game. Example: 'pygstudio release -o "C:/projects/python/releases/my small square"'
* `-x`, `--options`: the options for pyinstaller. This appends to your existing _default-pyinstaller-argument_ configuration.
* `-c`, `--confirm`: Skips prompts like overwrite project.
* `-s`, `--optimize-storage`: enable storage optimization by removing redundant dll's in the folder. 
    
    > Warning: Your game might break so use this at your own risk!

### Practical Uses
For your game to have a icon for the executable, you specify `-x` argument. Example:
`python -m pygstudio release -f "C:/projects/my game" -o "C:/releases/my game" -x '--icon "C:/projects/my game/game.ico"'`
