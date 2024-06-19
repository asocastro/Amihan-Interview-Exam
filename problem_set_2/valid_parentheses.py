# Checks if the input string is valid if closed properly
def isValid(s: str) -> str:
    # Dictionary to jot down number of opening and closing brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Traverse through each character in the string
    for char in s:
        if char in matching_bracket.values():  # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in matching_bracket.keys():  # If it's a closing bracket
            if stack == [] or matching_bracket[char] != stack.pop():  # Check if it matches the top of the stack
                return "Invalid"
        else:
            # In case there are characters other than '()', '{}', '[]'
            return "Invalid"
    # If stack is not empty, returns "invalid"
    if stack != []:
        return "Invalid"
    
    # Else returns "valid"
    return "Valid"

if __name__ == "__main__":
    # Test Cases
    test_case_1 = "()"
    test_case_2 = "([])"
    test_case_3 = "("
    test_case_4 = "([)]"
    test_case_5 = "]"
    test_case_6 = "}(){"
    
    
    # Method calls
    print(isValid(test_case_1)) # valid
    print(isValid(test_case_2)) # valid
    print(isValid(test_case_3)) # invalid
    print(isValid(test_case_4)) # invalid
    print(isValid(test_case_5)) # invalid
    print(isValid(test_case_6)) # invalid
