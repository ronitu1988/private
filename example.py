import time
from order import Order


# if __name__ == '__main__':
#     order = Order()
#     order.parse_json_order('orders.json')

#     while order.get_size_orders() > 0:
#         recieved_order = order.pull_two_order_per_second()
#         time.sleep(2)
#         print ("End of Cycle ....")
        

import time
import multiprocessing
import random

Queue = []

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x, q):
    y = x*x
    val= random.randrange(0,19)
    q.put(val)
    #size = q.qsize()
    print('{} squared results in a/an {} number | queue value {}'.format(x, basic_func(y), val))
    time.sleep(2)
    

def multiprocessing_func1(x, q):
    y = x*x
    value = q.get()
    while value is None:
        time.sleep(2)
        value = q.get()
    
    print('{} DEVICED results in a/an {} number | queue value {}'.format(x, basic_func(y), value))
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    q = multiprocessing.Queue()
    for i in range(0,10):
        
        p1 = multiprocessing.Process(target=multiprocessing_func1, args=(i,q))
        processes.append(p1)
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,q))
        processes.append(p)
        
        p.start()
        p1.start()
        
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))