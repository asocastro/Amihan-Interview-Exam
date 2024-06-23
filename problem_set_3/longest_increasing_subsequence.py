# Finds the length of the longest increasing subsequence in an array
def find_LIS(input_array) -> int:
    # Length of the input list
    length = len(input_array)
    # New array to put the values of the LIS
    array = [1] * length
    
    # Iterates from the right to the left of the list to find the LIS
    for i in range(length -1, -1, -1):
        for j in range(length -1, i, -1):
            if input_array[i] < input_array[j]:
                array[i] = max(array[i], array[j] + 1)
    
    # Returns the max value of the LIS
    return max(array)

if __name__ == "__main__":
    array = [10, 9, 2, 5, 3, 7, 101, 18]
    print(find_LIS(array))