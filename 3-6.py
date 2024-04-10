class SparseArray:
    def __init__(self):
        self.sparse_dict = {}

    def __setitem__(self, index, value):
        self.sparse_dict[index] = value

    def __getitem__(self, index):
        return self.sparse_dict.get(index, 0)

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i])) # Output: arr[0] = 0, arr[1] = 10, arr[2] = 0, arr[3] = 0, arr[4] = 0, arr[5] = 0, arr[6] = 0, arr[7] = 0, arr[8] = 20, arr[9] = 0
