from datetime import datetime
time=input("Enter time 12 hour format:")
d=datetime.strptime(time,"%I:%M %p")
print(d.strftime("%H:%M"))
