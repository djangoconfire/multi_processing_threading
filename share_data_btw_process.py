"""
    @author: RituRaj
    created: 3 May, 19

    Share data between processes using shared memory
        - shared memeory as - Array 
        - shared memory as - Value 
"""
import multiprocessing 

def cal_square(numbers, result):
    for idx , n in enumerate(numbers):
        result[idx] = n*n 
    print ("Inside Proess",result[:])

if __name__=="__main__":
    numbers = [2,3,4,5]
    # sharing data using shared memory 
    # result - shared memory variable 
    result = multiprocessing.Array('i',len(numbers))
     # Creare a main proess 
    # On creating a new process ,  a new address space is allocate to this process 
    p1 = multiprocessing.Process(target=cal_square,args=(numbers,result,))

    # start the process excetion 
    p1.start()
    # join the child proess with parent process 
    p1.join()

    print ("Result Outside Process",result[:])    
