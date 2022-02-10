import os
import csv

def create_csv(path):
    dir_path = '/'.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(path, "w+", newline='') as file:
        csv_file = csv.writer(file)
        head = ["Acc", "Edit", "F10", "F25", "F50"]
        csv_file.writerow(head)

def append_csv(path, metric_list):
    with open(path, "a+", newline='') as file:
        csv_file = csv.writer(file)
        datas = [metric_list]
        csv_file.writerows(datas)

