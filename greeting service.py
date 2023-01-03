import smtplib
import mysql.connector
import datetime



if __name__=="__main__":
    user="root"
    pwd="Ridd_hish"
    db="se"
    host="localhost"
    try:
        mycon=mysql.connector.connect(user=user,password=pwd,database=db,host=host)
        cursor=mycon.cursor()
    except:
        print("Error: Unable to connect to the database")
        exit()
