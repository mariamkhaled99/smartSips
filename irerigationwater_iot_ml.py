"""serial part using usb """
# import serial.tools.list_ports
# import serial
# import time
# import csv
# import random

# filename = 'IrrigationWater_Final_Dataset.csv'



# # print(random_row)

# ports = serial.tools.list_ports.comports()
# print(ports)
# data = serial.Serial('com7',9600)
# time.sleep(1)
# while True:
#     while (data.in_waiting==0):
#         pass
#     with open(filename, 'r') as f:
#         reader = csv.reader(f)
#         rows = list(reader)
#     random_row = random.choice(rows)
#     data_packet=data.readline()
#     data_packet=str(data_packet,'utf-8')
#     data_packet=data_packet.strip('\r\n')
#     data_packet = data_packet.split(',')
    
#    data=data_packet+random_row
        # print(data )



"""on the air connection part using wifi """


# import csv
# import random
# import socket
# import time 

# filename = 'DrinkingWater_Final_Dataset.csv'
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('0.0.0.0', 8585 ))
# s.listen(0)                 
 
# while True:
#     client, addr = s.accept()
#     client.settimeout(5)
#     while True:
#         content = client.recv(1024)
#         if len(content) ==0:
#            break
#         if str(content,'utf-8') == '\r\n':
#             continue
#         else:
#             # print(str(content,'utf-8'))
            
#             with open(filename, 'r') as f:
#                 reader = csv.reader(f)
#                 rows = list(reader)
#             random_row = random.choice(rows)
#             data = content.decode('utf-8')
#             # lines = data.splitlines()
#             # for line in lines:
#             #     print(line)
#             # data_packet=str(data_packet,'utf-8')
#             data_packet=data.strip('\r\n')
#             data_packet = data_packet.split(',')
#             data=data_packet+random_row
#             print(data )
#     client.close()


