from pathlib import Path
from PIL import Image
from rembg import remove
from os import walk
import datetime


def decorator(func):
    def png_decorator():
        start_time = datetime.datetime.now()
        print(f"Start process of the decorator in {str(start_time)[:-7]}.")
        pict = func()
        jpg_file = Image.open(f"{Path.cwd()}/pictures/{pict}")
        png_file = remove(jpg_file)
        png_file.save(f"{Path.cwd()}/from_decorator_folder/{pict[:-3]}png")
        print(
            f"The end of decorating process in {str(datetime.datetime.now())[:-7]}. Total using time is: "
            f"{str(datetime.datetime.now() - start_time)[:-7]}.")

    return png_decorator


@decorator
def picture():
    file_tuple = list(walk(f"{Path.cwd()}/pictures"))
    jpg_file = file_tuple[0][2][0]
    # print(jpg_file)

    return jpg_file


if __name__ == "__main__":
    picture()
