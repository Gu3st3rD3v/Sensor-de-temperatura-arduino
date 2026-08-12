import serial
import time 
import requests


arduino = serial.Serial("COM", 9600) # DEPOIS DO COM, COLOQUE O NUMERO NO QUAL O ARDUINO ESTÁ CONECTADO
time.sleep(2)

URL = "https://wttr.in/Cachoeiro%20dc%20Itapemirim?format=%t"

while True:
     temp = requests.get(URL).text.strip()
     arduino.write((temp + "\n").encode())
     print("Enviado:", temp
     time.sleep(10)
    
     
