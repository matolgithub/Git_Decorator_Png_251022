from pathlib import Path
from PIL import Image
from rembg import remove
from os import walk


def picture():
    file_tuple = list(walk(f"{Path.cwd()}/pictures"))
    jpg_file = file_tuple[0][2][0]
    print(jpg_file)

    return jpg_file


def png_decorator():
    file = picture()
    jpg_file = Image.open(f"{Path.cwd()}/pictures/{file}")
    png_file = remove(jpg_file)
    png_file.save(f"{Path.cwd()}/png_files/{file}[:-3].png")


def main():
    png_decorator()


if __name__ == "__main__":
    main()
