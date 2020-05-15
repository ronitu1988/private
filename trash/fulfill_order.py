import multiprocessing

class FulfillOrder():
    def __init__(self):
        # super(FulfillOrder, self).__init__()
        # self.mgr = multiprocessing.Manager()
        # self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()
        self.Queue = []

    def fulfillment(self, Order):
        with self.lock:
        #     self.active.append(Order)
            self.Queue.append(Order)
        self.count()

    def count(self):
        print("Number need to dispatch", len(self.Queue))