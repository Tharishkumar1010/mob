import os
from dotenv import load_dotenv 
import pymongo
from kafka import KafkaConsumer
import sys 
import json

load_dotenv()
# connection for local host
# bootstrap_servers=['localhost:9092'] 

# connection for cluster 
bootstrap_servers = ["kafka"]

topicName = 'topic'
# mongo db connection
# client = pymongo.MongoClient("mongodb://localhost:27017")
#mongo atlas connection
client = pymongo.MongoClient(os.getenv("mongouri"))  

mydb = client["data"]
mycoll = mydb["collection"]

try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')   
    for topic in consumer:
        topic = json.loads(topic.value) 
        data = mycoll.insert_one(topic)  
        print(data)
except KeyboardInterrupt:
    sys.exit()

