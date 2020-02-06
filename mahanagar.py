from datetime import datetime
from getpass import getpass
import requests
import json
import time
import csv

f = csv.writer(open("MahanagarData.csv", "a")) 

f.writerow(["id", "alarm", "ignition", "status", "io1", "io2", "io3", "io4", "distance", "totalDistance", "motion", "deviceId", "type", "protocol", "serverTime", "deviceTime", "fixTime", "outdated", "valid", "latitude", "longitude", "altitude", "speed", "course", "address", "accuracy", "network"])

def mahanagar():
    
    now = datetime.now()

    url = "http://117.121.237.226:8082/api/positions/"
    auth = ("mahanagar", "mahanagar")

    response = requests.get(url, auth=auth)

    datas = response.json()



    for data in datas:
        f.writerow([data["id"], data.get("attributes").get("alarm"), data["attributes"]["ignition"], data["attributes"]["status"], data["attributes"]["io1"], data["attributes"]["io2"], data["attributes"]["io3"], data["attributes"]["io4"], data["attributes"]["distance"], data["attributes"]["totalDistance"], data["attributes"]["motion"], data["deviceId"], data["type"], data["protocol"], data["serverTime"], data["deviceTime"], data["fixTime"], data["outdated"], data["valid"], data["latitude"], data["longitude"], data["altitude"], data["speed"], data["course"], data["address"], data["accuracy"],data["network"]])


while True:
    # Warning !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print("Calling ....")
    mahanagar()
    time.sleep(60)
