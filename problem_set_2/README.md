# Problem Set 2: Valid Parentheses
 ## Problem Description
The second problem set wants me to make a function which checks if the input strings of the different kinds of brackets are closed properly.

 ## Solution Overview
 The solution I went with is to make a function (<b>isValid()</b>) which creates a stack to list down which opening brackets came first so we can tell what closing brackets to expect and a dictionary to see which bracket is paired with what.

 The idea is that it will do the following:
`````
    1. Take the input string
    2. iterate the characters
    2.1 check if the character is a valid dict value
    2.1.1 if it isnt return false/invalid
    2.2 add to the stack if it is
    2.3 iterate until a closing bracket is found and keep adding to stack inorder
    2.4 if a closing bracket, is it at the top of the stack?
    2.4.1 if not return invalid
    2.5 pop value on top of stack
    2.6 iterate till finished
    3 Return valid/true if stack is empty else invalid/false
`````



 Functions used: 


 | Function  | Output |
| ------------- | ------------- |
|  `isValid(s: str)` | string "Valid" or "Invalid" |


 ## Instructions to Run the Code
1. Open the file valid_parentheses.py and you can change the test cases at lines 26 - 31 to whichever you want to test.
2. Most IDEs have a run button if you open the file but if you're going to run the script through cli, use the command: 
    ```python problem_set_2/valid_parentheses.py```
assumming you are at the root folder AMIHAN-INTERVIEW-EXAM