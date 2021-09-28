# import requests
# resp = requests.post('https://textbelt.com/text', {
#   'phone': '5555555555',
#   'message': 'Hello world',
#   'key': 'textbelt',
# })
# print(resp.json())

import zerosms
import getpass

def sendSms():
    nm = getpass.getpass("Enter username: ")
    pwd = getpass.getpass("Enter password: ")
    num = getpass.getpass("Receiver's number: ")
    zerosms.sms(phno=nm,passwd=pwd,message="hello world!!!",receivernum=num)

sendSms()