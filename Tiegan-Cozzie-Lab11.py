# -----------------------------------------------------
# CSCI 127, Lab 11                                    |
# November 9, 2021                                      |
# Tiegan Cozzie                               |
# -----------------------------------------------------

# Your solution goes here. ------------------------------

class Queue:
    def __init__(self, name):
        self.queue_name=name
        self.item=[]

    def enqueue(self, name):
        self.item.append(name)
    
    def __iadd__(self,item):
        self.item.append(item)
        return self 

    def dequeue(self):
        if len(self.item)!=0:
            pres=self.item[0]
            self.item.pop(0)
        return pres

    
    def is_empty(self):
        if len(self.item)==0:
            return True
    
    def __str__(self):
        final=""
        for name in self.item:
            final+=name+", "
        return "Queue: " + "[FIRST--> "+final+" <--LAST]"

    def is_equal(self, other):
        if(self.item==other.item):
            print("Equal")
        else:
            print("Not Equal")


# Do not change anything below. -------------------------

def main():
    presidents = Queue("Presidents")

    print("\nQueuing up G.Wash, J.Ad, T.Jeff, J.Mad, J.Mon")
    presidents.enqueue("Washington")
    presidents.enqueue("Adams")
    presidents.enqueue("Jefferson")
    presidents.enqueue("Madison")
    presidents.enqueue("Monroe")
    print(presidents)

    print("\nDequeue George -- first president in, so first one out")
    presidents.dequeue()
    print(presidents)

    print("\nDequeue everybody")
    while not presidents.is_empty():
        print("President dequeued:", presidents.dequeue())
        print(presidents)

    print("\nAdding J.Ad, A.Jack, M.Van, B.Harr, J.Ty")
    presidents.enqueue("Adams")
    presidents.enqueue("Jackson")
    presidents.enqueue("Van Buren")
    presidents.enqueue("Harrison")
    presidents.enqueue("Tyler")
    print(presidents)

    print("\nAdding J.Polk to the back of the line")
    presidents += "Polk" # See: https://www.python-course.eu/python3_magic_methods.php
    print(presidents)

    #TODO: add some code to test two queues for equality

# First Comparison
    other=Queue("Other")
    other.enqueue("Adams")
    other.enqueue("Jackson")
    other.enqueue("Van Buren")
    other.enqueue("Harrison")
    other.enqueue("Tyler")
    other +="Polk"
    print(other)

    presidents.is_equal(other)

# Second Comparison
    other=Queue("Other")
    other.enqueue("Tyler")
    other.enqueue("Harrison")
    other.enqueue("Van Buren")
    other.enqueue("Jackson")
    other.enqueue("Adams")
    other +="Polk"
    print(other)
    
    presidents.is_equal(other)

# Third Comparison
    other=Queue("Other")
    other.enqueue("Harry Truman")
    other.enqueue("Biden")
    other.enqueue("John Wilksbooth")
    other.enqueue("Washington")
    other.enqueue("Trump")
    other +="Polk"
    print(other)

    presidents.is_equal(other)
# -----------------------------------------------------

main()
