import os

os_name = os.name
print(f"Ваша операционная система: {os_name}")

current_path = os.getcwd()
print(f"Путь то текущей папки: {current_path}")

all_items = os.listdir(current_path)
files_only = []

for item in all_items:
    if os.path.isfile(item):
        files_only.append(item)

print(f"Найденные файлы в папке: {files_only}")

# for file in files_only:
#     name, extension = os.path.splitext(file)
    
#     if not extension:
#         continue

#     folder_name = (f"{extension[1:].upper()}_files")

#     os.makedirs(folder_name, exist_ok=True)

stats = {}

for file in files_only:
    name, extension = os.path.splitext(file)

    if not extension or file == os.path.basename(__file__):
        continue

    folder_name = (f"{extension[1:].upper()}_files")
    os.makedirs(folder_name, exist_ok=True)

    old_path = os.path.join(current_path, file)
    new_path = os.path.join(current_path, folder_name, file)

    file_size = os.path.getsize(old_path)

    os.rename(old_path, new_path)

    if folder_name not in stats:
        stats[folder_name] = [0,0]
    stats[folder_name][0] +=1
    stats[folder_name][1] += file_size

print("\n Статистика переноса:")
for folder, data in stats.items():
    count = data[0]
    size_mb = data[1] / (1024*1024)
    print(f"В папку {folder} перемещено {count} файлов, их сумарный размер - {size_mb:.4f} МБ")




print("\n Переименовывание файла")

target_folder = "TXT_files"
target_folder_path = os.path.join(current_path, target_folder)

if os.path.exists(target_folder_path):
    folde_files = os.listdir(target_folder_path)

    if folde_files:
        old_filename = folde_files[0]
        new_filename = f"renamed_{old_filename}"

        old_file_path = os.path.join(target_folder_path, old_filename)
        new_file_path = os.path.join(target_folder_path, new_filename)

        os.rename(old_file_path, new_file_path)

        print(f"Файл {old_file_path} был переименован в {new_file_path}")
    else:
        print(f"Папка {target_folder} пуста, ничего не изменилось.")
else:
    print(f"Папка {target_folder} не найдена.")





