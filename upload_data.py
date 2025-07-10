from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri="mongodb+srv://ceastinstark:WPcPFybCjfNZOJKk@cluster0.aglmeux.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

DATABASE_NAME='ceast'
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\win10\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)