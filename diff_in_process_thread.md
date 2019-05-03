### Difference in MultiProcessing and MultiThreading
- Multiprocessing and Multithreading both are way to achieve multitasking.
- Multitasking
    - Running more than one task at some time. 
- MultiPrcessing
    - Running more than one process at same time. 
    - processes can't share their own addess space.
    - To share their address space , there should be IP techniques to share data between processes.
    - benefits
        - if there is any error or memory leak won't hurt he execution of another process.
- Multithreading
    - Running more than one thread inside a process.
    - Each thread have their address space and shareble between other threads inside a process. 
    - Disadvantage
        - If there is any error or memory leak in any of thread will hurt the execution of other threads and hence , the execution of program. 
    


