import os
import csv
import shutil

def get_rel(file_path:str,copy_path:str) -> str:
    path = os.path.join(os.path.commonpath([file_path,copy_path]),"")
    rel=copy_path.replace(path,"")
    return rel

def task2(dataset:str,copy_path:str)->None:
    file_path = os.path.dirname(__file__)
    path = os.path.join(copy_path,"short_dataset")
    if not os.path.exists(path):
        os.makedirs(path)
    file = os.path.join(copy_path,"annotation_for_short.csv")
    f=open(file, 'w')
    writer=csv.writer(f,delimiter=',',lineterminator='\n')
    for fold in os.listdir(dataset):
        for file in os.listdir(os.path.join(dataset,fold)):
            orig = os.path.join(dataset,fold,file)
            new = os.path.join(path,fold+"_"+file)
            shutil.copyfile(orig,new)
            relative = get_rel(file_path,new)
            row = [orig,relative,fold]
            writer.writerow(row)

