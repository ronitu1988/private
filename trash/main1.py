import time
import json
import multiprocessing
import random

from orders import Order
# from fulfill_order import FulfillOrder

def parseJson(file_name):
    '''
    parse and ingest json data from orders.json
    '''
    list_orders = []
    with open(file_name) as json_file:
        data = json.load(json_file)
        for item in data:
            list_orders.append(
                Order(
                    item['id'],
                    item['name'],
                    item['temp'],
                    item['shelfLife'],
                    item['decayRate'],
                )
            )
    return list_orders

# def recived_order(order, Dispatch):
#     """thread worker function"""
#     for i in order:
#         print (i.id)
#         Dispatch.fulfillment(order)
#     print("_----------_")
#     #time.sleep(30)
#     return

# if __name__ == '__main__':
#     list_order = parseJson("orders.json")
#     print(len(list_order))

#     Dispatch = FulfillOrder()

#     for index in range(0,len(list_order),2):
#         p = multiprocessing.Process(target=recived_order, args=(list_order[index:index+2],Dispatch))
#         p.start()
#         time.sleep(2)



# import multiprocessing

# class MyFancyClass(object):
    
#     def __init__(self, name):
#         self.name = name
#         self.queue = []
    
#     def do_something(self):
#         proc_name = multiprocessing.current_process().name
#         print ('Doing something fancy in %s for %s!' % (proc_name, self.name))
#         self.queue.append(proc_name)
#         self.count()

#     def count(self):
#         print("Number of length : ", len(self.queue))


# def worker(q):
#     obj = q.get()
#     obj.do_something()


# if __name__ == '__main__':
#     queue = multiprocessing.Queue()

#     for i in range(10):
#         p = multiprocessing.Process(target=worker, args=(queue,))
#         p.start()
    
#         queue.put(MyFancyClass('Fancy Dan'))
        
#     # Wait for the worker to finish
#     queue.close()
#     queue.join_thread()
#     p.join()

class Queue():
    def __init__(self):
        self.queue_dispatch = []

    def add_queue_dispatch(self, item):
        self.queue_dispatch.append(item)
    
    def get_size_dispatch(self):
        return len(self.queue_dispatch)
    
    def get_queue_dispatch(self):
        return self.queue_dispatch

class Reciever(Queue):
    def __init__(self):
        self.queue = []
        self.counting = 0
        self.dispatch = Dispatch()

    def count(self):
        self.counting+=1
        self.dispatch.fulfill("A")
        print("Ready to Dispatch : ", self.counting)
 
    def print(self):
        print(self.counting)


class Delivery():
    def __init__(self):
        self.queue = []
        self.counting = 0
    
    def count(self):
        self.counting+=1
        

    def print(self):
        print(self.counting)

class Dispatch(Queue):
    def fulfill(self,item):
        self.add_queue_dispatch(item)
        print("Recieved Order and Fulfill : ", self.get_queue_dispatch())

    def pull(self):
        print ("Another Worker is Pull from Queue : ", len(self.get_queue_dispatch()))
        if len(self.get_queue_dispatch()) > 0:
            print("POPing queue for delivery")

    def print(self):
        print(len(self.get_queue_dispatch()))

if __name__ == '__main__':
    list_order = parseJson("orders.json")

    dispatch = Dispatch()
    reciever = Reciever()
    delivery = Delivery()

    count = 0
    while (count <10):
        # creating processes 
        p1 = multiprocessing.Process(target=reciever.count())
        p2 = multiprocessing.Process(target=dispatch.pull()) 
        #p3 = multiprocessing.Process(target=delivery.count())

        count +=1
    
  
        # starting process 1 
        p1.start() 
        # starting process 2 
        p2.start() 
    
        # wait until process 1 is finished 
        p1.join() 
        # wait until process 2 is finished 
        p2.join() 
    

    #dispatch.print()
    reciever.print()
    delivery.print()
    # both processes finished 
    print("Done!")
