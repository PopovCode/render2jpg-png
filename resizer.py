from glob import glob
import os

from PIL import Image

RESOLUTIONS = [
    (2850, 2500),
    (1114, 980),
    (800, 704),
]

def resize2png(file, new_image_size):
    for size in new_image_size:
        image = Image.open(file)
        original_wight, original_height = image.size
        wight, height = size
        index_resolution = new_image_size.index(size) + 1
        out_path = "./files/output/png/"
        os.makedirs(out_path, exist_ok=True)
        out_file_name = out_path + file.split("\\")[-1][:-4] + f'({index_resolution}).png'

        if (original_wight == wight and original_height == height):
            image.save(out_file_name, "PNG")
        else:
            resized_image = image.resize((wight, height))
            resized_image.save(out_file_name, "PNG")

        print(f'[INFO] Файл {out_file_name} успешно сохранен')
        image.close()

def resize2jpg(file, new_image_size):

    for size in new_image_size:
        image = Image.open(file)
        original_wight, original_height = image.size
        wight, height = size
        index_resolution = new_image_size.index(size) + 1
        out_path = "./files/output/jpg/"
        os.makedirs(out_path, exist_ok=True)
        out_file_name = out_path + file.split("\\")[-1][:-4] + f'({index_resolution}).jpg'

        if (original_wight == wight and original_height == height):
            image.save(out_file_name, "JPEG", quality=100)
        else:
            resized_image = image.resize((wight, height))
            resized_image.save(out_file_name, "JPEG", quality=100)

        print(f'[INFO] Файл {out_file_name} успешно сохранен')
        image.close()

def resizer(resolutions):
    for file in glob('./files/input/*.tif'):
        print("\n[INFO] Обработка " + file.split('\\')[-1])
        resize2jpg(file=file, new_image_size=RESOLUTIONS)
        resize2png(file=file, new_image_size=RESOLUTIONS)




if __name__ == "__main__":
    resizer(resolutions=RESOLUTIONS)