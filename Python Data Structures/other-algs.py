import numpy as np

def binary_search(nums: list[int], target: int, min_idx: int=None, max_idx: int=None):
    """
    Input list should be sorted. Returns the index of the value desired. 
    If the target value does not exist, returns None.
    """
    if min_idx is None: min_idx = 0
    if max_idx is None: max_idx = len(nums) - 1
    while min_idx <= max_idx:
        mid_idx = min_idx + (max_idx - min_idx) // 2

        if nums[mid_idx] == target: 
            return mid_idx
        elif nums[mid_idx] < target:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx - 1
        
    return None

if __name__ == '__main__':
    print('=== BINARY SEARCH TESTING ===')
    nums_list = [-39,-18,-5,-3,-1,0,1,2,3,5,16,21,28]
    nums_list_2 = sorted(np.random.randint(low=-500, high=500, size=100))
    
    target_idx = binary_search(nums_list, target=30)
    assert target_idx == None

