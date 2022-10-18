import socket    
import json 
from kafka import KafkaProducer

s = socket.socket() 

# cluster host connection
HOST = "socket"

# local host connection 
HOST="127.0.0.1"
PORT = 12345    
s.connect((HOST,PORT))
# local host connection
# bootstrap_servers=['localhost:9092'] 

# cluster connection
bootstrap_servers = ["kafka"] 
topicName = 'topic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 3,value_serializer=lambda m: json.dumps(m).encode('utf-8')) 
while True:  
    try:
        data=s.recv(70240).decode()
        json_acceptable_string = data.replace("'", "\"") 
        json_data = json.loads(json_acceptable_string)
        print(json_data)
        for Json in json_data:
            producer.send(topicName,Json)
            print(Json)
    except Exception as e:
        print(e)
s.close()
        