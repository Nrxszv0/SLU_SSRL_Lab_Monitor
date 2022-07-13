# Lab_Monitor
Lookup the data sheet for the DHT22 and determine which of the three pins are Signal, Ground, and VCC

You can control the pi via ssh.
Type "ifconfig" into the terminal on the pi to find the ip address.
The ip is 165.134.26.142.
Type "ssh ssrl-pi@165.134.26.142" into terminal.
The password is "SSRLPi1$".
When you are entering the password into terminal it will look like you are not typing.

Enter "cd Desktop".
Enter "cd LabMonitor".
Enter "python3 LabEnvironmentMonitor.py".

You can press tab to autocomplete a filename.

However, the program should start on startup.

You can change the text message/email recipient in the sendMessages function in LabEnvironmentMonitor.py.

This website will show how to send text message emails.
https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/

<img width="460" alt="SetupLabMonitor" src="https://user-images.githubusercontent.com/58677365/178592039-ef6bb5be-3b50-461f-a991-085efd3bb47a.PNG">

<img width="532" alt="Pinout" src="https://user-images.githubusercontent.com/58677365/178784648-888082ad-56e1-4326-bcf7-c659bf10fa5b.PNG">
<img width="1086" alt="NewMonitorSchematic" src="https://user-images.githubusercontent.com/58677365/178806578-e1876546-636d-460b-bb36-d2236d33e93a.png">
