import os

def get(dataset:str,rait:str,count:int) ->str:
    for fold in os.listdir(dataset):
        if fold == rait:
            absolute = os.path.join(dataset,fold)
            all_rait = os.listdir(absolute)
            return os.path.join(absolute, all_rait[count])
    return None    




if __name__ == '__main__':
    print(get("C:\Proganiy\Git PP\dataset","5",3))