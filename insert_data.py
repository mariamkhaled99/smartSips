import csv
import sqlite3


conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
with open('DrinkingWater_Final_Dataset.csv', 'r') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        c.execute("INSERT INTO ml_api_mlhome (pH, sodium, magnesium, calcium, chloride, potassium ,carbonate,sulphate,eC,tH,wQI,Potability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",row )
        c.execute("UPDATE ml_api_mlhome SET ph = 7.54 WHERE id= 1")
        conn.commit()
c.close()


conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
with open('IrrigationWater_Final_Dataset.csv', 'r') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        c.execute("INSERT INTO ml_api_mlfarm (rSC, pI,kr,mH, na, sAR,sSP ,eC,iWQI,USABLE) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",row )
        c.execute("UPDATE ml_api_mlfarm SET rSC = -0.21 WHERE id= 1")
        conn.commit()
c.close()

 



# fix customuser empty field error

# conn = sqlite3.connect("db.sqlite3")
# c = conn.cursor()
# c.execute("DELETE FROM user_api_customuser  WHERE id= 3 " )
# conn.commit()
# c.close()  