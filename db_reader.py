# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:09:59 2021

@author: snf52211
"""


import sqlite3
import pandas as pd

con=sqlite3.connect("C:/Users/snf52211/Desktop/ENE425/flask_db_write/superuser.db")

cur=con.cursor()

# query="""INSERT INTO users(user,password)
#             VALUES('gab','gab')"""

# cur.execute(query)

query2="""SELECT * FROM global"""
df=pd.read_sql(query2,con)
# con.commit()
con.close()