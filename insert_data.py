import csv
import sqlite3


conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
with open('DrinkingWater_Final_Dataset.csv', 'r') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        c.execute("INSERT INTO ml_api_mlhome (pH, sodium, magnesium, calcium, chloride, potassium ,carbonate,sulphate,eC,tH,wQI,Potability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",row )
        conn.commit()
c.close()


conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
with open('IrrigationWater_Final_Dataset.csv', 'r') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        c.execute("INSERT INTO ml_api_mlfarm (rSC, pI,kr,mH, na, sAR,sSP ,eC,iWQI,USABLE) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",row )
        conn.commit()
c.close()

 
# UPDATE ml_api_mlhome SET ph = 7.54 WHERE id= 1;
# UPDATE ml_api_mlfarm SET rSC = -0.21 WHERE id= 1;
    