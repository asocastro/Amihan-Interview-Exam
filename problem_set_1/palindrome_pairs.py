# Concatenates all possible pairs excluding pairing with itself and creates a list
# of its indices
def concatenate_pairs(input_list) -> tuple:
    new_input_list = []
    index_list = []
    n = len(input_list)
    
    # For each item in input_list pair it once with every other item in input_list
    for i in range(n):
        for j in range(n):
            if i != j:
                new_input_list.append(input_list[i] + input_list[j])
                index_list.append((i, j))
    # Returns new list
    return new_input_list, index_list

# Checks the input list for palindromes using a splice method and also makes a list 
# of the palindromes indices
def check_for_palindrome(input_list, index_list) -> tuple:
    palindrome_list = []
    palindrome_index_list = []
    
    # Iterates the list and checks for palindromes using the splice method [::-1] 
    # (Reverses string)
    for i, x in enumerate(input_list):
        if x == x[::-1]:
            palindrome_list.append(x)
            palindrome_index_list.append(index_list[i])
    # Returns palindrome list
    return palindrome_list, palindrome_index_list

if __name__ == "__main__":
    # Test Case
    strings = ["abc", "cba", "def", "ca", "ac"]
    
    # Method calls
    print("For the strings: " + str(strings))
    
    pairs, indices = concatenate_pairs(strings)
    print("The possible pairs are: " + ', '.join(pairs))
    print(indices)
    
    palindromes, new_indices = check_for_palindrome(pairs, indices)
    print("and the palindromes are: " + ', '.join(palindromes))
    print("with indices:" + str(new_indices))
