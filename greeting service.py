import mysql.connector
import datetime
from twilio.rest import Client
import smtplib

def todaysBirthdays():
    cursor.execute("SELECT * FROM USER_DATA")
    todaysBirthdays = cursor.fetchall()
    for i in todaysBirthdays:
        dob=i[-1]
        if dob.month==today.month and dob.day==today.day:
            continue
        else:
            todaysBirthdays.remove(i)
    return todaysBirthdays


def sendBirthdayMail(birthdays):
    for i in birthdays:
        name=i[0]
        eMail=i[1]
        print(name,eMail)
        server.sendmail(senderEmail, eMail, "Happy Birthday " + name)
    print("Birthday mails sent to ", len(birthdays),"users")


def sendFestiveGreetings():
    cursor.execute("select t1.name,t1.email,t2.festival_name from user_data t1 natural left outer join festivals t2 where t2.Date=curdate()")
    data=cursor.fetchall()
    for i in data:
        eMail = i[1]
        name = i[0]
        festival = i[2]
        server.sendmail(senderEmail, eMail, "Happy "+festival+name+". Wishing you a prosperous and happy "+festival)


def sendBirthdayMsg(birthdays):
    accSID = "<Twilio Accound SID>"
    authToken = "<twilio AUTH token>"
    twilioCli = Client(accSID, authToken)
    myTwilioNumber = '+15672863118'
    for i in birthdays:
        name=i[0]
        phone=i[2]
        message=twilioCli.messages.create(body="Happy Birthday"+name,from_=myTwilioNumber,to=phone)
    print("Birthday messages sent to ", len(birthdays),"users")


if __name__=="__main__":
    user="root"
    pwd="<db_password>"
    db="se"
    host="localhost"
    today=datetime.date.today()
    try:
        mycon=mysql.connector.connect(user=user,password=pwd,database=db,host=host)
        cursor=mycon.cursor()
    except:
        print("Error: Unable to connect to the database")
        exit()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # connecting to SMTP server at port 587
        server.ehlo()
        server.starttls()
        senderEmail = '<senderEmail>'
        senderPass = '<senderPassword>'
        server.login(senderEmail, senderPass)
    except:
        print("Unable to connect to the SMTP server")
        exit()
    todaysBirthdays = todaysBirthdays()
    sendFestiveGreetings()
    sendBirthdayMail(todaysBirthdays)
