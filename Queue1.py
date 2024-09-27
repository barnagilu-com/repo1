"""
Program to demonstrate functionality of queue
"""

class Queue(object):
    def __init__(self):
        self.queue = []
        #self.head = 0

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue1(self):
        if self.queue == []:
            return "Queue is empty"
        else:
            val = self.queue[0]
            for i in range(0, len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()
            return val
    def is_empty(self):
        return self.queue == []

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue.pop(0)



obj = Queue()
print(obj.dequeue())
obj.enqueue((10))
obj.enqueue(20)
obj.enqueue(30)
print(obj.queue)
print(obj.dequeue())
print(obj.queue)
obj.enqueue(40)
print(obj.queue)
print(obj.dequeue())
obj.enqueue(50)
print(obj.queue)
print(obj.dequeue())
obj.enqueue(60)
print(obj.dequeue())
obj.enqueue(70)
print(obj.dequeue())
print(obj.queue)

