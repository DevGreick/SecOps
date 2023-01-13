import os 
import time 

while True: 
    response = os.system("ping -c 1 google.com")

    if response == 0: 
        print ("Google está acessível") 
    else: 
        print ("Google não está acessível")

    time.sleep(300)