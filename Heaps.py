import Tree_funcs_classes as TFC

class Heap:
    def __init__(self, name, root):
        self.name = name
        self.arr = [root]

    def combine_heaps(self, i):
        max = i
        left = 2*i + 1
        right = 2*i + 2

        if len(self.arr) > left:
            if self.arr[left] > self.arr[max]:
                max = left
        if len(self.arr) > right:
            if self.arr[right] > self.arr[max]:
                max = right
        
        if i != max:
            parent = self.arr[i]
            child = self.arr[max]
            self.arr[i] = child
            self.arr[max] = parent
            self.combine_heaps(max)

    def build_max_heap(self):
        n = len(self.arr)
        for i in range(int(n/2)-1, -1, -1):
            self.combine_heaps(i)

                
    def add_node(self, node):
        self.arr.append(node)
        self.build_max_heap()     
            
# def max_heapify(array):
#         for i in range(len(array) - 1, -1, -1):
#             child = array[i]
#             print(i)
#             if i % 2 == 0:
#                 a = int((i-2)/2)
            
#             else:
#                 a = int((i-1)/2)
                
#             print(a)
#             parent = array[a]

#             if parent < child:
#                 array[i] = parent
#                 array[a] = child
#         return array

# Test tree
test_tree = [6, 8, 3, 9, 2, 1, 10, 12, 11, 4, 5, 7]
t_tree = Heap('test', 6)

for u in test_tree: 
    t_tree.add_node(u)

print(t_tree.arr)


# test_heap = max_heapify(test_tree)

# def max_heapify2(array, ind):
#     left_child = 2*ind + 1
#     right_child = 2*ind + 2
#     arr = array.copy()
#     if len(arr) > left_child:
#         if arr[ind] < arr[left_child]:
#             parent = arr[ind]
#             child = arr[left_child]
#             array[ind] = child
#             array[left_child] = parent
#         max_heapify2(arr, left_child)

#         if len(arr) > right_child:
#             if arr[ind] < arr[right_child]:
#                 parent = arr[ind]
#                 child = arr[right_child]
#                 array[ind] = child
#                 array[right_child] = parent
#             max_heapify2(arr, right_child)
    
#     return arr

# test_heap = max_heapify2(test_tree, 0)

# print(test_heap)
