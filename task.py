import streams
import threading

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
mutex4 = threading.Lock()

def initTask():
    mutex1.release()
    mutex2.acquire()
    mutex3.acquire()
    mutex4.acquire()

def task1(number, delay):
    mutex1.acquire()
    print("mot1")
    mutex2.release()

def task2(number, delay):
    mutex2.acquire()
    print("mot2")
    mutex3.release()

def task3(number, delay):
    mutex3.acquire()
    print("mot3")
    mutex4.release()

def task4(number, delay):
    mutex4.acquire()
    print("mot4")
    mutex1.release()