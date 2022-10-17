import random
import re
import smtplib

def isEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex,email):
        return True
    else:
        return False

def generateOTP(n):
    otp=""
    for i in range(n):
        otp+=str(random.randint(0,9))
    return(otp)

def verifyOTP(otp,OTP):
    if OTP==otp:
        print("Email ID successfully verified...")
    else:
        print("Invalid OTP")

if __name__=='__main__':
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        senderEmail='root.rvl@gmail.com'
        senderPass='gdpmznhjhqijiuas'
        server.login(senderEmail,senderPass)
    except:
        print("Unable to connect to the SMTP server")
        exit()
    n=int(input("Enter the OTP length: "))
    otp=generateOTP(n)
    for i in range(3):
        eMail=input("Enter email id: ")
        if isEmail(eMail):
            break
        else:
            print("Invalid email id!!!")
    else:
        print("You've entered an invalid email too many times!!! \n Try again later...")
        exit()
    server.sendmail(senderEmail,eMail,"Subject:OTP\nYour OTP for is "+otp)
    print("An {} digit OTP has been sent to {}".format(n,eMail))
    print("Verify your email id: ")
    OTP=input("Enter the OTP: ")
    verifyOTP(otp,OTP)
    server.close()