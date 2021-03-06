import streams
import threading
import adc

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
mutex4 = threading.Lock()

def initTask(): #0111
    mutex1.release() 
    mutex2.acquire()
    mutex3.acquire()
    mutex4.acquire()

def task1(number, delay): #1011
    while True:
        mutex1.acquire()
        print("mot1")
        mutex2.release()
        sleep(delay)

def task2(number, delay): #1101
    while True:
        mutex2.acquire()
        print("mot2")
        mutex3.release()
        sleep(delay)

def task3(number, delay): #1110
    while True:
        mutex3.acquire()
        print("mot3")
        mutex4.release()
        sleep(delay)

def task4(number, delay): #0111
    while True:
        mutex4.acquire()
        print("mot4")
        mutex1.release()
        sleep(delay)
        
    
def taskADC():
    while True:
        print("One sample:",adc.read(A5))
        sleep(1000)
        
        
        
        
        