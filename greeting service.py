import smtplib
import mysql.connector
import datetime

# birthday la mail
#

def sendMail(msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # connecting to SMTP server at port 587
        server.ehlo()
        server.starttls()
        senderEmail = 'root.rvl@gmail.com'
        senderPass = 'gdpmznhjhqijiuas'
        server.login(senderEmail, senderPass)
    except:
        print("Unable to connect to the SMTP server")
        exit()

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
