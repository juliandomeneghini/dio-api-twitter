from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["dio"]  # Troque o nome "dio" pelo nome do seu banco de dados

trends_collection = db["trends"]

