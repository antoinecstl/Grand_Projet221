import time

second = time.time()
while True : 
    second2 = time.time() - second
    time2 = round(second2,2)
    print(time2, end = "\r")
    