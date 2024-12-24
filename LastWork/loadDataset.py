import kagglehub
import pandas as pd
import json
from functools import reduce

# Download latest version
@staticmethod
def getDataset() -> str:
    """
    возращает адрес скаченного dataset
    """
    return kagglehub.dataset_download("praneshchowdhury/top-10000-anime-dataset-2024")

@staticmethod
def get_Dataset2jsonType(namefile:str):
    df:pd.DataFrame = pd.read_csv(namefile)
    newDF:list[dict] = [{f"{k}":df[k][i] for k in df.keys()} for i in range(10000)]
    for i in range(10000):
        #перевод типов из np в python
        newDF[i]["Rating"] = float(newDF[i]["Rating"]) 
        newDF[i]["Ranked"] =   int(newDF[i]["Ranked"])
    
    return newDF

