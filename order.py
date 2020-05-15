import json
import time
import random

from fulfillment import Fulfillment

class OrderType():
    def __init__(self, id, name, temp, shelfLife, decayRate):
        self.id = id
        self.name = name
        self.temp = temp
        self.shelfLife = shelfLife
        self.decayRate = decayRate
        self.cTime = time.time()
        self.shelfLifeValue = None

class Order ():
    

    def __init__(self):
        #list_orders = []
        self.list_order_data = []
        

    def parse_json_order(self, file_name):
        '''
        parse and ingest json data from orders.json
        '''
        with open(file_name) as json_file:
            data = json.load(json_file)
            for item in data:
                self.list_order_data.append(
                    OrderType(
                        item['id'],
                        item['name'],
                        item['temp'],
                        item['shelfLife'],
                        item['decayRate'],
                    )
                )
            self.list_orders = self.list_order_data[:10]
        return self.list_order_data[:10]

    def pull_two_order_per_second(self, queue, data):
        print ("\n\nPulled {recieved} order & Remaining Json Order : {remaining}".format(
            recieved=len(data[0]),
            remaining=len(data[1])
        ))
        self._dispath_order(queue, data[0])

    def get_size_orders(self, list_orders):
        return len(list_orders)

    def _dispath_order(self, queue, orders):
        for order in orders:
            print (" Order recived ID: ", order.id, order.temp)
            queue.put(order)
            print("\n")
        time.sleep(2)

    def process_order(self, queue, args):
        orders = args[0]
        total_orders = args[1]

        print ("ORDER: Pulled {recieved} order & Remaining Orders : {remaining}".format(
            recieved=len(orders),
            remaining=len(total_orders)
        ))

        if len(orders) != 0:
            for order in orders:
                print ("+   Order recived ID: ", order.id, order.temp)
                queue.put(order)
            time.sleep(2)

    def test_order(self, queue, list_orders):
        value = [list_orders.pop() for i in range(2)]
        print ("ORDERD: recieved {} - {}".format(value, len(list_orders)))
        queue.put(value)
        time.sleep(2)
    