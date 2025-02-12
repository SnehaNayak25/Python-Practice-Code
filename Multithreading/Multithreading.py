import time
import threading
print(threading.current_thread())
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigits(li1):
    print(threading.current_thread())
    for i in li1:
        print(i)
        time.sleep(2)

def displayAlpha(li2):
    print(threading.current_thread())
    for i in li2:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=displayDigits,args=(li1,),name = "Developer")
t2 = threading.Thread(target=displayAlpha,args=(li2, ),name="Tester")

t1.start()
t1.join()
t2.start()