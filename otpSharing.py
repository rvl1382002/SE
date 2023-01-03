import random # Random library to generate OTP
import re #Using regular expression library to check if email is in valid format
import smtplib #to send e-mail

def isEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #setting email template: *@*.*
    if re.fullmatch(regex,email): #checking if the entered email matches the template
        return True
    else:
        return False

def generateOTP(n): #function to return a OTP of length n
    otp=""
    for i in range(n):
        otp+=str(random.randint(0,9))
    return(otp)

def verifyOTP(otp,OTP): #Function to verify if entered OTP is correct
    if OTP==otp:
        print("Email ID successfully verified...")
    else:
        print("Invalid OTP")

if __name__=='__main__':
    # try block to check if connection can be established with the smtp server
    try:
        server=smtplib.SMTP('smtp.gmail.com',587) #connecting to SMTP server at port 587
        server.ehlo()
        server.starttls()
        senderEmail='<sender email id>'
        senderPass='<sender password>'
        server.login(senderEmail,senderPass)
    except:
        print("Unable to connect to the SMTP server")
        exit()
    n=int(input("Enter the OTP length: "))
    otp=generateOTP(n)
    for i in range(3): # Stop the program if user enters a invalid email several times
        eMail=input("Enter email id: ")
        if isEmail(eMail):
            break
        else:
            print("Invalid email id!!!")
    else:
        print("You've entered an invalid email too many times!!! \n Try again later...")
        exit()
    server.sendmail(senderEmail,eMail,"Subject:OTP\nYour OTP for is "+otp) #Sending the email
    print("An {} digit OTP has been sent to {}".format(n,eMail))
    print("Verify your email id: ")
    OTP=input("Enter the OTP: ")
    verifyOTP(otp,OTP)
    server.close()

