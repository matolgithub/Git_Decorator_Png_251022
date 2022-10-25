from pathlib import Path
from PIL import Image
from rembg import remove
from os import walk

print(Path.cwd())
print(walk(Path.cwd()))
