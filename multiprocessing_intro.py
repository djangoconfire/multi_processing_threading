"""
    @author: RituRaj
    created: 3 May, 19

    Basics of multithreading 
"""
import time 

def cal_square(numbers):
    print ("sqaure of numbers")
    for n in numbers:
        time.sleep(0.2)
        print ("Square:", n*n)

def cal_cube(numbers):
    print ("Cube of the numbers")
    for n in numbers:
        time.sleep(0.2)
        print ("Cube:",n*n*n)

numbers = [2,3,4,5]

t1 = time.time()

# Here functions are called sequential
cal_square(numbers)
cal_cube(numbers)

print ("Time of Eecution:",time.time() - t1)


# Using Threading module  
import threading 

t1 = time.time()
# create a separe thread for each function 
thread1 = threading.Thread(target=cal_square,args=(numbers,))
thread2 = threading.Thread(target=cal_cube,args=(numbers,))

# start the thread 
thread1.start()
thread2.start()

# join the each thread with main thread 
thread1.join()
thread2.join()

print ("Execution time using threading",time.time() - t1)
