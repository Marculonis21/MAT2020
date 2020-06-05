#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(host='localhost',
                       user='matskolnik',
                       password='matskolnik',
                       db='skola',
                       charset='utf8mb4')

cursor = conn.cursor()

prijmeni = input("Zadej příjmení absolventa: ")
jmeno = input("Zadej jméno studenta: ")

s1 = ""
if(prijmeni != ""):
    s1 = "abs.prijmeni=\"{}\" and".format(prijmeni)
s2 = ""
if(jmeno != ""):
    s2 = "abs.jmeno=\"{}\" and".format(jmeno)

sql = "SELECT * from abs,profesor,tridni WHERE {} {} abs.rokmat=tridni.rokmat and abs.para=tridni.para and abs.stdel=tridni.stdel and tridni.id_prof=profesor.id_prof;".format(s1,s2)

cursor.execute(sql)
result = cursor.fetchall()

for line in result:
    print("Student: {} {}".format(line[1],line[2]))
    print("Maturitní třída: {}.{} {}".format(line[5],line[6],line[4]))
    print("Třídní učitel: {} {} {}".format(line[11],line[9],line[10]))
    print()
    
