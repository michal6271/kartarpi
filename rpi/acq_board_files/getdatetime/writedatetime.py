from datetime import datetime
import time

while 1:


   
    f = open("/var/www/html/currentdt.txt", "w+")

    f.write(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-5])

    f.close()

    time.sleep(0.1)
