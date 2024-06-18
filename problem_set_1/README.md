# Problem Set 1: Palindrome Pairs
 ## Problem Description
 The problem requires me to concatenate two distinct values/strings in a list and check if the pair is a palindrome. The expected output is a list of index pairs which are palindromes.

 ## Solution Overview
 The solution I went with is comprised of the following:
 1. Make a function (<b>concatenate_pairs</b>) which accepts a list of strings and make a new list with all possible combinations of distinct pairs and another list containing the indices of paired values/characters.

 2. Make a function (<b>check_for_palindrome</b>) accepts a list where we want to find the palindromes and a list of indices. The function will output a list of palindromes and the indices of the palindromes based on the original list.

 Functions used: 


 | Functions  | Outputs |
| ------------- | ------------- |
|  'concatenate_pairs(input_list)' | new_input_list, index_list  |
|  'check_for_palindrome(input_list, index_list)'  | palindrome_list, palindrome_index_list   |

 ## Instructions to Run the Code
1. Open the file palindrome_pairs.py and change the variable of strings at line 34 to whichever you want to test.
2. Most IDEs have a run button but if you're going to run the script through cli, use the command: <b>python problem_set_1/palindrome_pairs.py</b> assumming you are at the root folder AMIHAN-INTERVIEW-EXAM