import os
import csv

def get_rel(absolut:str,file:str) -> str:
    path = os.path.join(os.path.commonpath([absolut,file]))
    rel=absolut.replace(path,"")
    return rel
    

def task1(dataset: str, direct: str) -> None:
    path_f = os.path.dirname(__file__)
    file = os.path.join(direct,'annotation.csv')
    f=open(file, "w")
    writer=csv.writer(f,delimiter=',',lineterminator='\n')
    for i in os.listdir(dataset):
        fold = os.path.join(dataset, i)
        for otz_num in os.listdir(fold):
            absolute=os.path.join(fold,otz_num)
            relative=get_rel(absolute, path_f)
            writer.writerow([absolute,relative,i])

        
 


