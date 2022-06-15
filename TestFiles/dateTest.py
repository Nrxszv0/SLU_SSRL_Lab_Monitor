from datetime import datetime


now = datetime.now()
strDate = now.strftime("%m/%d/%Y %H:%M:%S")
print(strDate)