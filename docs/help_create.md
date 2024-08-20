## Documentation: Pygstudio Create

`pygstudio create` takes one positional argument `NAME` which is your project name.
This copies a predefined template to your project destination (default='.')
Example: `pygstudio create "my small square"`.

### Optional Arguments
* `-o`, `--output`: The output directory of your project. Example: `pygstudio create "my small square" -o "C:/projects/python"`
* `-c`, `--confirm`: Skips prompts like overwrite project.
* `-x`, `--exclude-additional-files`: Excludes additional files that may be added in the project. This will skip the process of including additional files specified by `pygstudio config --additional-create-path PATH`