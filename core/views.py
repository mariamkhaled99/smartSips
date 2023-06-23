# import json
# from django.http import JsonResponse
# from core.mqtt import client as mqtt_client
# import requests
# import serial
# import time
# import csv
# import random

# def iot_client():
#     filename = 'IrrigationWater_Final_Dataset.csv'
#     # ser = serial.Serial('com6',9600)
#     # time.sleep(1)
#     # while True:
#     #     while (ser.in_waiting==0):
#     #         pass
    
#     with open(filename, 'r') as f:
#         reader = csv.reader(f)
#         rows = list(reader)
#         random_row = random.choice(rows)
#         data=random_row
#         print(random_row )
        
#         return data

#     # line = ser.readline()
#     # data = str(line,'utf-8')
#     # data=data.strip('\r\n')
#     # data = data.split(',')
    
        

# msg = iot_client()
# url = 'https://smartsips-production.up.railway.app/publish_message'
# data = {'topic': 'test_project_iot', 'msg': msg}
# headers = {'Content-type': 'application/json'}
# response = requests.post(url, data=json.dumps(data), headers=headers)
# time.sleep(6)

# def publish_message(request):
#     request_data = json.loads(request.body)
#     rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
#     return JsonResponse({'code': rc})
