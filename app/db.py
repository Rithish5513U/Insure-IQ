from dotenv import load_dotenv
import pandas as pd
from pymongo import MongoClient
import os

load_dotenv()

uri = os.getenv('MONGO_URI')

client = MongoClient(uri)
db = client['medical_cost_db']
collection = db['medical_costs']