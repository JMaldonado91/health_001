from __future__ import print_function
import csv
import mysql.connector

print("MySQL_Schema.csv")
conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="1315", db="project_j")
cursor = conn.cursor()

sql= """DROP TABLE IF EXISTS `health_001`; CREATE TABLE `health_001` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `county` varchar(25) NOT NULL,
  `restaurants` decimal(10,0) NOT NULL,
  `population` decimal(10,0) NOT NULL,
  `percentage` decimal(19,2) NOT NULL,
  PRIMARY KEY (`id`))"""
cursor.execute(sql)

with open('MySQL_Schema.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['id'], row['county'], row['restaurants'], row['population'], row['percentage'])
       
        conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="1315", db="project_j")
        sql_statement = "INSERT INTO health_001(id,county,restaurants,population,percentage) VALUES (%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['id'], row['county'], row['restaurants'], row['population'], row['percentage'])])
        
        conn.commit()
        
cursor.close()       
conn.close()

