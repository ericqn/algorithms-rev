class MaxHeap:
    def __init__(self, root:int=None, start_cap:int=16):
        if not root: self.root = 0
        else: self.root = root

        self.capacity = start_cap
        self.data = [None] * self.capacity
        self.num_items = 0
    
    def insert(self, value:int):
        if self.num_items == 0:
            self.data[0] = value
            self.num_items += 1
            return
        
        if self.num_items == self.capacity:
            self.data += [None] * self.capacity
            self.capacity *= 2
        
        self.data[self.num_items] = value
        self.bubble_up(value)
        self.num_items += 1
    
    def bubble_up(self, value):
        cur_idx = self.num_items
        parent_idx = (cur_idx - 1) // 2

        while parent_idx >= 0 and self.data[parent_idx] < value:
            self.data[cur_idx] = self.data[parent_idx]
            self.data[parent_idx] = value

            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2

    def pop(self):
        value_to_return = self.data[0]
        final_value = self.data[self.num_items-1]
        self.data[self.num_items-1] = None
        self.data[0] = final_value
        self.num_items -= 1

        self.bubble_down(final_value)
        return value_to_return
    
    # TODO:
    def bubble_down(self, value):
        cur_idx = 0
        left_child_idx, right_child_idx = 1, 2

        while self.data[left_child_idx] or self.data[right_child_idx]:
            left_val = self.data[left_child_idx]
            right_val = self.data[right_child_idx]
            if self.data[left_child_idx] and self.data[right_child_idx]:
                val_to_idx = {left_val: left_child_idx, right_val:right_child_idx}
                max_child_val = max(left_val, right_val)
                max_child_idx = val_to_idx[max_child_val]

                self.data[cur_idx] = max_child_val
                self.data[max_child_idx] = value
                cur_idx = max_child_idx
            elif left_val and value < left_val:
                self.data[cur_idx] = left_val
                self.data[left_child_idx] = value
                cur_idx = left_child_idx
            elif right_val and value < right_val:
                self.data[cur_idx] = right_val
                self.data[right_child_idx] = value
                cur_idx = right_child_idx
            else:
                break
                
            left_child_idx = 2*cur_idx+1
            right_child_idx = 2*cur_idx+2

    def __len__(self):
        return self.num_items

    def __str__(self):
        return str(self.data[:self.num_items])

if __name__ == '__main__':
    test_heap = MaxHeap()

    for i in range(0, 25, 2):
        test_heap.insert(i)
    test_heap.pop()
    test_heap.pop()
    test_heap.pop()
    test_heap.pop()
    print(test_heap)