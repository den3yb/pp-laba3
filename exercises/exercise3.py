import os
import csv
import shutil
import random


def get_rel(file_path: str, copy_path: str) -> str:
    path = os.path.join(os.path.commonpath([file_path, copy_path]), "")
    rel = copy_path.replace(path, "")
    return rel


def task3(
    dataset: str,
    copy_path: str,
):
    file_path = os.path.dirname(__file__)
    path = os.path.join(copy_path, "random_dataset")
    if not os.path.exists(path):
        os.makedirs(path)
    file = os.path.join(copy_path, "annotation_for_random.csv")
    f = open(file, "w")
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    random_list = random.sample(list(range(1, 10000)), 3000)
    count = 0
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    for fold in os.listdir(dataset):
        for file in os.listdir(os.path.join(dataset, fold)):
            orig = os.path.join(dataset, fold, file)
            copy = os.path.join(path, str(random_list[count]))
            count += 1
            relative = get_rel(file_path, copy)
            shutil.copyfile(orig, copy)
            writer.writerow([orig, relative, fold])


