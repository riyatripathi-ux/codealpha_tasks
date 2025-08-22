import os
import shutil

source = "source_folder"
destination = "images_folder"

# Create destination if not exists
os.makedirs(destination, exist_ok=True)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))
        print(f"Moved: {file}")
