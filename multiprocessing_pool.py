"""
    @auhtor: RituRaj
    created: 3 May , 19

    Pool(Map or Reduce)
        - Map - mapping task to more than one core
        - Reduce - aggregating the result 
"""
from multiprocessing import Pool 

def func(x):
    return x*x


if __name__=="__main__":
    inputs = [2,3,4,5,3,4,5,3,4,5]
    p = Pool()
    output = p.map(func,inputs)
    print (output)