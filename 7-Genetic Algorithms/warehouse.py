import numpy as np

class Warehouse:
    def __init__(self, items, ID):
        self.warehouseID = ID
        self.items = items
        
    def addItem(self, item):
        if item not in self.items:
            self.items = np.append(self.items, item)
        
    def removeItem(self, item):
        if item in self.items:
            self.items = np.delete(self.items, np.where(self.items==item))