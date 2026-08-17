from abc import ABC,abstractmethod
class Notification(ABC):
    def send(self,message):
        print("Common")
    def send(self,message,message2,message3=0):
        print(message,message2,message3)
class EmailNotification(Notification):
    def send(self,message):
        print(f"Email Notification sent as {message}")
class SMSNotification(Notification):
    def send(self,message):
        print(f"Sms Notification sent as {message}")
class WhatsappNotification(Notification):
    def send(self,message):
        print(f"Whatsapp Notification sent as {message}")
class PushNotification(Notification):
    def send(self,message):
        print(f"Push Notification sent as {message}")
queries=[
    WhatsappNotification(),
    EmailNotification(),
    SMSNotification(),
    PushNotification()]
for query in queries:
    message=input()
    query.send(message)
obj=EmailNotification()
print(obj.send("dsfs","sfddsf"))
