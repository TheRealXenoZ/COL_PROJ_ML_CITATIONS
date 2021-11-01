import sys
import csv
import os
#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='apri1')

import sqlite3
con = sqlite3.connect('phiscls1')

cur = con.cursor()
cur.execute('SELECT * FROM firstset;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('firstset1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('firstset1.csv file successfully created')
cur.execute('SELECT * FROM secondset;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('secondset1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('secondset1.csv file successfully created')
con.commit()

