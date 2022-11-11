import requests
import json

URL="http://127.0.0.1:8000/RestApt/"
def get_data():
    data={}
    
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)


get_data()