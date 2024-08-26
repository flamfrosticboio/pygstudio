import shutil, os

pygstudio_path = os.path.abspath(os.path.join(__file__, "..", "..", "pygstudio"))

folder = os.path.join(pygstudio_path, "_addons")
if not os.path.exists(folder):
    raise RuntimeError("Cannot pack addons if folder does not exist.")

remove_paths = [os.path.join(folder, "__pycache__")]
for path in remove_paths:
    if os.path.exists(path):
        print(f"Removing {path}")
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)

shutil.make_archive(os.path.join(pygstudio_path, "addons"), "zip", folder)
print("Operation was successful")
