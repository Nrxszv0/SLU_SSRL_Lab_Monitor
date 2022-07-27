import csv

fields = ["Date", "Time", "Temperature", "Temperature Warning", "Humidity", "Humidity Warning"]

with open('test2.csv', 'a') as f:
    w = csv.writer(f)
    w.writerow(fields)
    for i in range(10):
        w.writerow([i, "12:12:23", "23C", "High Temp", "445%", "hIGH hUMIDIty"])

