import win32com.client as win32
import csv

with open('ACM Members - Sheet1.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines[1])

outlookApp = win32.Dispatch('Outlook.Application')
nameSpace = outlookApp.GetNameSpace('MAPI')

new_mail = outlookApp.CreateItem(0)

new_mail.Subject = "tester email" 
new_mail.Bodyformat = 1

new_mail.Body = "I am testing my mail bot"

#new_mail.Sender = "nathan.rusch@marquette.edu"
new_mail.To = "nathan.rusch@marquette.edu"

new_mail.Send()

print("success")