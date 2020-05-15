import time
import random

from shelf import Shelf

class Fulfillment():
    def fulfill(self, queue, shelfStorage):
        while queue[0].empty():
            time.sleep(random.randint(0,2))

        order = queue[0].get()
       
        order.shelfLifeValue = self._calc_shelf_life(order)
        print("FULFILL:  order -[ ID:{id} | Name:{name} | shelfLifeValue: {value} ]".format(
            id=order.id,
            name=order.name,
            value=order.shelfLifeValue
        ))


        Shelf().storage_shelf(shelfStorage, order)

        # print (order.temp)
        # print (shelfStorage[order.temp] , type(shelfStorage[order.temp]))
        # #list_temp = shelfStorage[order.temp]
        # shelfStorage[order.temp] = shelfStorage[order.temp] + [order]
        #storage_queue.put(order)
        

        # print("shelfStorage : ", shelfStorage)
        time.sleep(random.randint(4,6))
        queue[1].put(order)

        #self.shelf.storage_shelf(order)
        

    def _calc_shelf_life(self,order):
        orderAge = time.time() - order.cTime
        if order.temp in ["HOT", "COLD", "Frozen"]:
            shelfDecayMofidier = 1
        else:
            shelfDecayMofidier = 2
        value = (order.shelfLife - (order.decayRate * orderAge * shelfDecayMofidier)) / order.shelfLife
        return value

    def test_fulfillment(self, queue):
        value = queue.get()
        print("Value fulfill order : {} ", value)
        while value is None:
            time.sleep(1)
            value = queue.get()

        print("Dispatch & Ready for pick up : {} ", value)