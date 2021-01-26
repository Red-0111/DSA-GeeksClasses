"""
Print a sequence of numbers starting with N where A[0] = N, without using loop, 
in which  A[i+1] = A[i] - 5,  until A[i] > 0. After that A[i+1] = A[i] + 5  
repeat it until A[i] = N.

Example 1:

Input: N = 16
Output: 16 11 6 1 -4 1 6 11 16
Explaination: The value decreses until it 
is greater than 0. After that it increases 
and stops when it becomes 16 again.
Example 2:

Input: N = 10
Output: 10 5 0 5 10
Explaination: It follows the same logic as 
per the above example.
Your Task:
You do not need to read input or print anything. Your task is to complete the 
function pattern() which takes N as input parameters and returns a list 
containing the pattern.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 104 

"""


#User function Template for python3

#using loops
class Solution:
    def pattern(self, N):
        # code here
        result = []
        x = N
        while (x > 0):
            result.append(x)
            x -= 5
        while (x <= N):
            result.append(x)
            x += 5
        return result


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends