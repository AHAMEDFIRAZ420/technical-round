def find_median_sorted_arrays(array1, array2):
    if len(array1) > len(array2):
        array1, array2 = array2, array1
    
    size1, size2 = len(array1), len(array2)
    total_size = size1 + size2
    half_size = total_size // 2
    
    low, high = 0, size1
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = half_size - cut1
        
        left1 = float('-inf') if cut1 == 0 else array1[cut1 - 1]
        right1 = float('inf') if cut1 == size1 else array1[cut1]
        
        left2 = float('-inf') if cut2 == 0 else array2[cut2 - 1]
        right2 = float('inf') if cut2 == size2 else array2[cut2]
        
        if left1 <= right2 and left2 <= right1:
            if total_size % 2 == 1:
                return min(right1, right2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    
    return 0.0

print("Find Median of Two Sorted Arrays")
print("Enter numbers separated by spaces")
print("Example: 1 3 5")
print()

first_array = list(map(int, input("First sorted array: ").split()))
second_array = list(map(int, input("Second sorted array: ").split()))

median_value = find_median_sorted_arrays(first_array, second_array)
print(f"The median is: {median_value}")