from genericpath import isdir, isfile
import pandas as pd
import os

print("[+] You should drag the folder containing the extracted json files into the window to copy the path.")
json_dir = input("Json Directory:")
csv_xlsx = str(input("CSV or XLSX?:")).lower()

# default
_type = "csv"

if csv_xlsx == "csv":
    _type = "csv"
if csv_xlsx == "xlsx":
    _type = "xlsx"
# make a csv directory
if not isdir(_type):
    os.makedirs(_type)

# for file in (os.listdir(json_dir)):
#     print(file)
# exit()

for file in (os.listdir(json_dir)):

    file_name, file_extension = os.path.splitext(file)

    if file_extension == ".json":

        if os.path.isfile(f"{json_dir}//{file}"):
            print(f"Skipping {file} - File already exists.")
            continue

        print(f"Converting {file} to {file}_converted.{_type}")
        with open(f"{json_dir}//{file}", encoding='utf-8') as inputfile:
            df = pd.read_json(inputfile)
        
        if _type == "xlsx":
            df.to_excel(f"{_type}//{file}_converted.{_type}", encoding='utf-8', index=False)
        if _type == "csv":
            df.to_csv(f"{_type}//{file}_converted.{_type}", encoding='utf-8', index=False)
    else:
        print(f"Skipping {file} - Not a JSON.")