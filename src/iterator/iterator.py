#iterator.py

class Aggregate:
    """Has a list of detected objects, returns an iterator for it"""
    def __init__(self):
        self._list = None

    def __iter__(self):
        return Iterator(self._list)
  
    def get(self, index):
        return self._list[index]

    def set(self, l):
        self._list = l
        
class Iterator:
    """Implements the iterator"""
    def __init__(self, aggregate):
        self._list = aggregate
        self._size = len(aggregate)
        self._index = 0
    
    def __iter__(self):
        return self
  
    def __next__(self):
        if self._index < self._size:
            pos = self._index
            self._index += 1
            return aggregate.get(pos)
        else:
            raise StopIteration()


if __name__ == "__main__": 
    aggregate = Aggregate()  
    aggregate.set(["Person","Car","Dog","Cat"])
  
    for value in aggregate:
        print("Item: " + str(value))
