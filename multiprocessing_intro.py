"""
    @author: RituRaj
    created: 3 may, 19

    Multiprocessing basics 
        - Every process has its own address space (virtual memory).
        - Program variables are not shared between two processes.
        - You need to use IPC techniques(inter process communication) to share data between processes. 
"""
import time 
import multiprocessing 

square_result = []
def cal_square(numbers):
    global square_result
    for n in numbers:
        print ("Square:",str(n*n))
        square_result.append(n*n)
    print ("Inside the process",square_result)
    

if __name__=="__main__":
    numbers = [2,3,4,5]
    # cretae a process 
    p1 = multiprocessing.Process(target=cal_square,args=(numbers,))
    # start the execution of process
    p1.start()

    # join  the sub process to main process 
    p1.join()
    print ("Outside the process",square_result)
    print ("excution done ")
    
