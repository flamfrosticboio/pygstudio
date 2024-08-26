import shutil, os

pygstudio_path = os.path.abspath(os.path.join(__file__, "..", "..", "pygstudio"))

template_folder = os.path.join(pygstudio_path, "_template")
if not os.path.exists(template_folder):
    raise RuntimeError("Cannot pack template if template folder is none.")

remove_paths = [
    os.path.join(pygstudio_path, "template.zip"),
    os.path.join(pygstudio_path, "template"),
    os.path.join(pygstudio_path, "_template", "__pycache__"),
]
for path in remove_paths:
    if os.path.exists(path):
        print(f"Removing {path}")
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)

shutil.make_archive(os.path.join(pygstudio_path, "template"), "zip", template_folder)
print("Operation was successful")
