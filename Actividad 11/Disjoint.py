class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

def main():
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    parent = {}

    for v in vertices:
        parent[v] = v

    print("Make Set")
    print(parent)
    ds = DisjointSet(vertices, parent)

    ds.union('h', 'b')
    print(ds.find('h')) # prints d (OK)
    ds.union('h', 'i')
    print(ds.find('i')) # prints i (expecting d)

#main()


A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C= {1, 2, 3}

print('A U B =', A.union({'(10,200)'}))

#Agregar#
A.add('(10,400)')
print(A)

#el elemento r no se encuentra en a
print(A.isdisjoint('(10,400)'))

#print('B U C =', B.union(C))

#print('A U B U C =', A.union(B, C))

#print('A.union() = ', A.union())
