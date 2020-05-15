import random
import time

class ShelfLife():
    def __init__(self, id, name, value, temp):
        self.id = None
        self.name = None
        self.value = None
        self.temp = None

class Shelf():
    @staticmethod
    def storage_shelf(storage_queue, order):
        print("SHELF-STORAGE:  volume [ Hot : {hot} | Cold: {cold} | Frozen: {frozen} | Overflow: {overflow} ]".format(
                                hot=len(storage_queue['hot']),
                                cold=len(storage_queue['cold']),
                                frozen=len(storage_queue['frozen']),
                                overflow=len(storage_queue['overflow']),
                            ))
        print("SHELF-STORAGE:  Store order in {temp} Shelf - ID:{id} Name:{name} shelfLifeValue: {value}".format(
            temp=order.temp,
            id=order.id,
            name=order.name,
            value=order.shelfLifeValue
        ))
        if order.temp == "hot" and len(storage_queue['hot']) < 10:
            storage_queue['hot'] = storage_queue['hot'] + [order]
        elif order.temp == "cold" and len(storage_queue['cold']) < 10:
            storage_queue['cold'] = storage_queue['cold'] + [order]
        elif order.temp == "frozen" and len(storage_queue['frozen']) < 10:
            storage_queue['frozen'] = storage_queue['frozen'] + [order]
        else:
            #self._rearrange()
            if len(storage_queue['overflow']) < 15:
                storage_queue['overflow'] = storage_queue['overflow'] +[order]
            else:
                print("SHELF-STORAGE:  No more room available for {id} - {name}".format(id=order.id, name=order.name))
    
    def _rearrange(self):
        return True
 