"""
    @author: RituRaj
    created: 3 AMy ,19 

    Multiprocessing lock
        - we need a lock to preserve the access of resource at the same time 
            - e.g : Bathroom 
"""
import multiprocessing 

# Banking System

# Deposit money 
def deposit(balance,lock):
    for i in range(100):
        # putting lock here - critical section 
        lock.acquire()
        balance.value = balance.value + 1
        # releasing the lock 
        lock.release()

# withdraw money 
def withdraw(balance,lock):
    for i in range(100):
        # putting the lock here
        lock.acquire()
        balance.value = balance.value - 1
        # releasing the lock
        lock.release()

if __name__=="__main__":
    # shared memory valiable as Value 
    balance = multiprocessing.Value('i', 200)
    # Lock Variable 
    lock = multiprocessing.Lock()
    # create a new process 
    d = multiprocessing.Process(target=deposit, args=(balance,lock,))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock,))
    # start the child process
    d.start()
    w.start()
    # join the child proces with parent process
    d.join()
    w.join()

    print ("Balance:",balance.value)
    
