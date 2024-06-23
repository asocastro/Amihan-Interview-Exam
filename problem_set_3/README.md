# Problem Set 3: Longest Increasing Subsequence (LIS)
 ## Problem Description
The last problem I am tasked with is to produce an output of the length of the LIS in a given array. 

 ## Solution Overview
For the last challenge, I thought of a brute force method where I iterate all the indexes, store their values, compare if the values are greater than or less than the previous value so that I can create a list of increasing subsequences. However, I came across the term dynamic programming and decided to give it a shot. The solution I went with is that the pointer starts counting from the last value in the input array and starts comparing from there. It then starts comparing backwards towards the start of the array and builds the list from there so that it will only have to add the already counted values to the uncounted values.


 Functions used: 
 | Function  | Output |
| ------------- | ------------- |
|  `find_LIS(List: int)` | Returns the highest value of the longest increasing subsequence |


 ## Instructions to Run the Code
1. Open the file longest_increasing_subsequence.py and you can change the test cases at line 18 to whichever you want to test.
2. Most IDEs have a run button if you open the file but if you're going to run the script through cli, use the command: 
    ```python problem_set_3/longest_increasing_subsequence.py```
assumming you are at the root folder AMIHAN-INTERVIEW-EXAM