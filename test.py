import threading
import time

def loop():
        while True:
            print("loop")
            time.sleep(1)

def stop():
    while True:
         key = input("enter the key")
         if key == "q":
              exit()

if __name__ =="__main__":
    t1 = threading.Thread(target=loop)
    t2 = threading.Thread(target=stop)

    t1.start()
    while True:
         key = input("enter the key")
         if key == "q":
              t1.join()
              exit()