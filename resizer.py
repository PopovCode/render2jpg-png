from glob import glob
import os
import click


from PIL import Image

RESOLUTIONS = [
    (2850, 2500),
    (1114, 980),
    (800, 704),
]

def resize2png(file, resolutions, input_folder):
    for size in resolutions:
        image = Image.open(file)
        original_wight, original_height = image.size
        wight, height = size
        index_resolution = resolutions.index(size) + 1
        out_path = f"{input_folder}\output\png\\"
        os.makedirs(out_path, exist_ok=True)
        out_file_name = out_path + file.split("\\")[-1][:-4] + f'({index_resolution}).png'

        if (original_wight == wight and original_height == height):
            image.save(out_file_name, "PNG")
        else:
            resized_image = image.resize((wight, height))
            resized_image.save(out_file_name, "PNG")

        # print(f'[INFO] Файл {out_file_name} успешно сохранен')
        image.close()

def resize2jpg(file, resolutions, input_folder):
    for size in resolutions:
        image = Image.open(file)
        original_wight, original_height = image.size
        wight, height = size
        index_resolution = resolutions.index(size) + 1
        out_path = f"{input_folder}\output\jpg\\"
        os.makedirs(out_path, exist_ok=True)
        out_file_name = out_path + file.split("\\")[-1][:-4] + f'({index_resolution}).jpg'

        if (original_wight == wight and original_height == height):
            image.save(out_file_name, "JPEG", quality=100)
        else:
            resized_image = image.resize((wight, height))
            resized_image.save(out_file_name, "JPEG", quality=100)

        # print(f'[INFO] Файл {out_file_name} успешно сохранен')
        image.close()

def renaming_processed_files_final_dir(path):
    """Функция заменяет именя файлов с fileName(откр1)(1) -> fileName(откр1)"""

    files_path = f"{path}output\\**\*.*"
    replase_str = "(откр1)("
    for file in glob(files_path):
        if replase_str in file:
            # print(f'{file} - найдено совпадение')
            new_file_name = file.replace(replase_str, "(откр")
            # print(f'новое имя файла{new_file_name}\n')
            os.rename(file, new_file_name)

@click.command()
@click.option("--path", prompt="Input directory", help="Put your input directory.", default="d:\\tmp\\test\\")
@click.option("--out_format", prompt="Input out_format (1 - JPEG; 2 - PNG)", default="all", help="Select out_format(1 - 'JPEG', 2 - 'PNG'). Default all - JPEG+PNG")

def main(path, out_format):
    input_folder = f"{path}\*.tif"
    count_files = len(glob(input_folder))
    count_completed_files = 0
    print("\n")
    for file in glob(input_folder):
        file_name = file.split('\\')[-1]
        print(f"[INFO] Обработка {file_name} {count_completed_files+1}/{count_files}")
        if (out_format == "all"):
            resize2jpg(file=file, resolutions=RESOLUTIONS, input_folder=path)
            resize2png(file=file, resolutions=RESOLUTIONS, input_folder=path)
        elif (out_format == "1"):
            resize2jpg(file=file, resolutions=RESOLUTIONS, input_folder=path)
        elif (out_format == "2"):
            resize2png(file=file, resolutions=RESOLUTIONS, input_folder=path)
        count_completed_files += 1

    renaming_processed_files_final_dir(path)

    print(f'\n Всего обработано {count_completed_files} из {count_files} файлов.')

if __name__ == "__main__":
    main()