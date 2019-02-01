import geocoder
g = geocoder.ip('me')
message="""Subject: Laptop Co-ordinates

The Device Was turned on at [{A},{B}]
"""
import smtplib, ssl
receiver_email="anand.2@iitj.ac.in"  #enter Email adress you want to recieve the Co-ordinates on
sender_email="disposable ID @gmail.com"    #enter your Email ID, and turn "allow less secure apps" to on
# PS : i propopose make a temp ID for sender's email, as you are compromising the security of it
port = 465
password = "password for disposable ID here"    #type your password here (obviously)

#send email

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.format(A=str(g.latlng[0]),B=str(g.latlng[1])))

#this part is to take your heat out
import webbrowser
webbrowser.open("google.com")
from pynput.keyboard import Controller,Key
import time
keyboard=Controller()
time.sleep(3)
#keyboard.press('Shift')
for char in 'fuck you':
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(0.35)
keyboard.press(Key.enter)
keyboard.release(Key.enter)