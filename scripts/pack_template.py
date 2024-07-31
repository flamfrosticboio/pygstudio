import shutil, os

pygstudio_path = os.path.abspath(os.path.join(__file__, "..", "..", "pygstudio"))

template_folder = os.path.join(pygstudio_path, "_template")
if not os.path.exists(template_folder):
    raise RuntimeError("Cannot pack template if template folder is none.")

zip_path = os.path.join(pygstudio_path, "template.zip")
if os.path.exists(zip_path):
    print("Removing existing template zip file")
    os.remove(zip_path)

shutil.make_archive(os.path.join(pygstudio_path, "template"), "zip", template_folder)
print("Operation was successful")