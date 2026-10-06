# Coding Q3 - Generate All Permutations of a String

# Problem Statement
# Given a string s of distinct lowercase characters, return a list of all possible permutations of s.
# You must implement the permutation generation from scratch using backtracking.
# Use of any built-in permutation library functions (e.g., itertools.permutations) is NOT allowed.
# The output list may be returned in any order.

# Constraints
# •	1 <= s.length <= 8
# •	All characters in s are distinct lowercase English letters
# •	Expected time complexity: O(n × n!)

# Open Test Cases (Visible to Candidate)
# Input:  s = "abc"
# Output: ["abc","acb","bac","bca","cab","cba"]  (any order)
 
# Input:  s = "ab"
# Output: ["ab","ba"]  (any order)

# Solution:

def prem_find(s):
    if len(s) == 1:
        return [s]
    
    result = []

    for i in range(len(s)):
        c = s[i]   

        rem = s[:i] + s[i + 1: ]

        for p in prem_find(rem):
            for j in range(len(p)):
                result.append(p[:j] + c + p[j:])
    
    return result

#complexity is n*n

s = input("enter string: ")
print(prem_find(s))