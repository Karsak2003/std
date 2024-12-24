from fastapi import FastAPI, Response, UploadFile, File
import uvicorn
import pandas as pd
import json
from LastWork.loadDataset import get_Dataset2jsonType
import random


nameFile:str = r"C:\Users\Karim\.cache\kagglehub\datasets\praneshchowdhury\top-10000-anime-dataset-2024\versions\2\top_anime_dataset.csv"

#! uvicorn main:app --reload 
#! http://localhost:3000

app = FastAPI()


@app.get("/metrics")
async def get_metrics():
# Return data as JSON
    return {"cpu_usage":0.8,"memory_usage":0.5}


@app.get("/countries-data")
async def test():
# Return data as JSON
    with open(r"PW4\countries-data.json") as file:
        return random.choices(json.load(file), k=5)

@app.get("/top-10000-anime-dataset-2024")
async def test2():
# Return data as JSON
    with open(r"LastWork\test1.json", "r+") as file:
        return random.choices(json.load(file), k=10)

@app.get("/test")
async def test3():
# Return data as JSON
    return get_Dataset2jsonType(nameFile)
