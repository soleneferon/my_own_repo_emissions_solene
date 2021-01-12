# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:18:27 2021

@author: snf52211
"""


import psycopg2
from psycopg2 import Error
import pandas as pd


# Connect to an existing database
connection = psycopg2.connect(user="fdpilcaempyzag",
                              password="2734408960e164b36d221f4aba1c6366a8aae1746e75f3b44f0a7e2dd5c62476",
                              host="ec2-54-170-100-209.eu-west-1.compute.amazonaws.com",
                              port="5432",
                              database="d458bntp094mai",
                              sslmode='require')

# Create a cursor to perform database operations
cursor = connection.cursor()

# ##Table creation +++++++++++++++++
query_table='''CREATE TABLE backup(id serial PRIMARY KEY, 
                                    kms float4 , 
                                    transport varchar,
                                    fuel varchar,
                                    date varchar,
                                    co2 float4,
                                    ch4 float4,
                                    user_name varchar,
                                    updated varchar,
                                    group_name varchar)'''
# cursor.execute(query_table)
# connection.commit()

##Insert++++++++++++++++++++++++++
# query_insert= """INSERT INTO users(user_name,password)
#                 VALUES('gab','gab')"""
               
# cursor.execute(query_insert)
# connection.commit()

##Select++++++++++++++++
query_select='''SELECT * FROM global'''        
df=pd.read_sql(query_select,connection)  