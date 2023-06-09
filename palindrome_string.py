'''
Question:
Given a string S, check if it is palindrome or not.

Example 1:

Input: S = "abba"
Output: 1
Explanation: S is a palindrome
Example 2:

Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome
 

Your Task:
You don't need to read input or print anything. Complete the function isPalindrome()which accepts string S and returns an integer value 1 or 0.

Expected Time Complexity: O(Length of S)
Expected Auxiliary Space: O(1)


Constraints:
1 <= Length of S<= 105
'''
class Solution:
    def isPalindrome(self, S):
        return 1 if S[:] == S[::-1] else 0 

# for run in python IDE
  S=input()
  if(S==S[::-1]):
    print(1)
  else:
    print(0)
