# Use the `csv` module to read in and count the different file types.
import csv
import json

csv_file_path = "03_file-input-output/file-counter/filecounts.csv"
json_file_path = "03_file-input-output/file-counter/filecounts.json"

with open(json_file_path, "r") as json_file:
     data = json.load(json_file)
     field_names = list(data.keys())
     print(field_names)
     
with open(csv_file_path, "r") as file_in:
     reader = csv.DictReader(file_in, fieldnames=field_names)
     reader_list = list(reader)
     print(reader_list)
     
# check how much ".png" is presented:
png_count = data[".png"]
print(png_count)