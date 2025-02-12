import time
import threading
print(threading.current_thread())
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigits(li1):
    for i in li1:
        print(i)
        time.sleep(1)

def displayAlpha(li2):
    for i in li2:
        print(i)
        time.sleep(1)

displayDigits(li1)
displayAlpha(li2)