import os    
import time 
destination = 'H:\\My Drive\\new'
for item in os.listdir(destination):
    while item.endswith('.opdownload'):
        print(item)
        time.sleep(1)
        continue


