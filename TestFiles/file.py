from datetime import datetime


now = datetime.now()
strDate = now.strftime("%m-%d-%Y-%H:%M:%S")

fileName = "LabData/"  +"Test-" + strDate + ".txt"

f = open(fileName, 'a')
f.write("\nTest test ets test ets ets")
f.close()
