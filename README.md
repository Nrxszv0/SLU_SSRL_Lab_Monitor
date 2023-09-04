# Lab_Monitor
This repository is for an environmental lab monitor made for Saint Louis University's Space Systems Research Lab's clean room. This device sends text and email notifications which describe the state of the clean room. Depending on different criteria, the device could control different devices to change the state of the lab. 

![SLU_LAB_LID_OFF](https://github.com/Nrxszv0/SLU_SSRL_Lab_Monitor/assets/58677365/bf05d93a-2c4b-4a72-b8ee-3103f6b2c04e)
![SLU_LAB_LID_On](https://github.com/Nrxszv0/SLU_SSRL_Lab_Monitor/assets/58677365/61cecd4b-a9c2-4398-826a-ee1eb086b0fa)
<img width="460" alt="SetupLabMonitor" src="[https://user-images.githubusercontent.com/58677365/178592039-ef6bb5be-3b50-461f-a991-085efd3bb47a.PNG](https://github.com/Nrxszv0/SLU_SSRL_Lab_Monitor/assets/58677365/61cecd4b-a9c2-4398-826a-ee1eb086b0fa)">


## Instructions
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
