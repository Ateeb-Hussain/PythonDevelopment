# from config import counter
from datetime import date
import os
import shutil
import sys

# This will define Todays Date to Program
today = date.today()
date1 = today.strftime("%d %B %Y")
day = int(today.strftime("%d"))
# print(day)

# This is to make sure that the file exists to transfer files to targeted folder
if(not os.path.exists("F:/Telegrapher.pk official/Telegrapher.pk Visual News")):
    os.mkdir("F:/Telegrapher.pk official/Telegrapher.pk Visual News")
    print("Created News Folder: ",date1)

destination_path = f"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}"
source_path = f"C:/Users/Khraab PC/Downloads"


config = "config.py"

# This will make a folder for a day
if(not os.path.exists(f"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}")):
    os.mkdir(f"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}")
    print("Created New Folder: News ", day,".")
    with open (os.path.join(destination_path, config), "w") as fp:
        fp.write("counter = 1")
        fp.close
    # pass

sys.path.insert(3, f"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}")
from config import counter

path = rf"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}/News {counter}"

elements = [ f for f in os.listdir(source_path) if f'n' in f.lower() ]

for index, element in enumerate(elements):
    source_file_path = os.path.join(source_path,element)
    if(not os.path.exists(f"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}/News {counter}")):
        os.mkdir(f"F:/Telegrapher.pk official/Telegrapher.pk Visual News/{date1}/News {counter}")
        # print(f"Created New Folder: News {counter}.")
        # pass

    shutil.move(source_file_path, path)

    # Gets new file name
    _, extension = os.path.splitext(element)

    # Construct new file name
    new_file_name = f"{index}"
    os.rename(os.path.join(path, element), os.path.join(path, f"{new_file_name}{extension}"))
print(path)

with open (os.path.join(destination_path, config), "w") as fp:
    i = counter + 1
    fp.write(f"counter = {i}")


if __name__ == '__main__':
    pass