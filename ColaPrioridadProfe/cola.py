from queue import PriorityQueue

pq=PriorityQueue()

#pq.put(10)
#pq.put(1)
#pq.put(2)
#pq.put(0)

#while not pq.empty():
 #   print(pq.get())


pq.put((1,('a','f')))
pq.put((2,('a','b')))
pq.put((2,('b','f')))
pq.put((0,('a','e')))
pq.put((1,('a','c')))
pq.put((2,('c','d')))
pq.put((1,('d','e')))
pq.put((1,('b','e')))

while not pq.empty():
    print(pq.get())