## Documentation: Pygstudio Config

`pygstudio config` takes either 3 positional arguments `[set | get | remove]`

`pygstudio config set` sets a configuration. 
With no keywords passed, it will do nothing.
To set a configuration, enter its configuration name and specify its value.
Example: `pygstudio config set --additional-create-path "C:/.config"`

`pygstudio config get` gets a configuration. 
With no keywords passed, it will list the whole configuration.
To get a specific configuration, pass its configuration name only.
Example: `pygstudio config get --additional-create-path`.

It also takes multiple configuration keys.
Example: `pygstudio config get --additional-create-path --default-pyinstaller-args ...`

`pygstudio config remove` resets a configuration.
With no keywords passed, it will do nothing.
To reset a configuration, enter its configuration name only.
Example: `pygstudio config remove --addition-create-path`


### Available Configuration Keys
* `--additional-create-path` _(additional_create_path) (default=None)_: Path that include folders/files to the new project when `pygstudio create` is called.
* `--default-pyinstaller-args` _(default_pyinstaller_args) (default="-w --noconfirm")_: Default pyinstaller args that is combined with 'pygstudio release -x'.