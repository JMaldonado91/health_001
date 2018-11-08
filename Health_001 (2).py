
# coding: utf-8

# In[1]:


import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='1315',
         host='127.0.0.1',
         database='project_j')

cur = conn.cursor()

query = ("SELECT id, county, restaurants, percentage, population from health_001")

cur.execute(query)

for (id, county, restaurants, population, percentage) in cur:
  print("{}, {}, {}, {}, {}".format(id, county, restaurants, population, percentage))

cur.close()
conn.close()

