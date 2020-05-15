import multiprocessing
import time
import json
import traceback

from order import Order, OrderType
from fulfillment import Fulfillment
from shelf import Shelf

def parse_json_order(file_name):
    '''
    parse and ingest json data from orders.json
    '''
    orders = []
    with open(file_name) as json_file:
        data = json.load(json_file)
        for item in data:
            orders.append(
                OrderType(
                    item['id'],
                    item['name'],
                    item['temp'],
                    item['shelfLife'],
                    item['decayRate'],
                )
            )
    return orders[:50]

if __name__ == '__main__':
    starttime = time.time()
    order_queue = multiprocessing.Queue()
    pickup_queue = multiprocessing.Queue()
    processes = []
    processes1 = []
    reciever = Order()
    shelfStorage = multiprocessing.Manager().dict()
    shelfStorage["hot"] = []
    shelfStorage["cold"] = []
    shelfStorage["frozen"] = []
    shelfStorage["overflow"] = []

    #pickup_queue.put(shelfStorage)
    # order_json = multiprocessing.Array('i', range(100))
    # order_json = reciever.parse_json_order('orders.json')
    data = parse_json_order('orders.json')
    print (shelfStorage)

    #v = multiprocessing.Value('i', shelfStorage)
       
    dispatch = Fulfillment()
    count = 0
    try:
        while len(data) > 0:
            ordered = [data.pop() for i in range(2) if len(data) > 0]
            receieve_order = multiprocessing.Process(target=reciever.process_order, args=(order_queue, (ordered, data)))
            processes.append(receieve_order)
            receieve_order.start()

            fulfillment = multiprocessing.Process(target=dispatch.fulfill, args=((order_queue, pickup_queue), shelfStorage))
            processes1.append(fulfillment)
            fulfillment.start()
        
        for process in processes:
            process.join()

        for process in processes1:
            process.join()

        print ("SIZE : ", len(processes + processes1))
        time.sleep(10)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
    except Exception:
        print("Caught Everything")
        traceback.print_exc()
    finally:
        for process in processes:
            process.terminate()
    

    print("FINAL VALUE [ Hot : {hot} | Cold: {cold} | Frozen: {frozen} | Overflow: {overflow} ]".format(
                                hot=len(shelfStorage['hot']),
                                cold=len(shelfStorage['cold']),
                                frozen=len(shelfStorage['frozen']),
                                overflow=len(shelfStorage['overflow']),
                            ))
    print('That took {} seconds'.format(time.time() - starttime))