import os
import csv
import shutil

def get_rel(file_path:str,copy_path:str) -> str:
    path = os.path.join(os.path.commonpath([file_path,copy_path]),"")
    rel=copy_path.replace(path,"")
    return rel

def main(dataset:str,copy_path:str,name:str)->None:
    file_path = os.path.dirname(__file__)
    f=open(name, "w")
    writer=csv.writer(f,delimiter=',',lineterminator='\n')
    for fold in os.listdir(dataset):
        for file in os.listdir(os.path.join(dataset,fold)):
            orig = os.path.join(dataset,fold,file)
            new = os.path.join(copy_path,fold+"_"+file)
            shutil.copyfile(orig,new)
            relative = get_rel(file_path,new)
            row = [orig,relative,fold]
            writer.writerow(row)



if __name__ == '__main__':
    main("C:\Proganiy\Git PP\dataset","C:\Proganiy\pp-laba2\dataset_short","annotation_for_copy.csv")