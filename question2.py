# Coding Q2 - Minimum Window Substring

# Problem Statement
# Given two strings s and t, return the shortest contiguous substring of s that contains all characters of t including duplicates.
# If no such substring exists, return an empty string "". The answer is guaranteed to be unique when it exists.

# Constraints
# •	1 <= s.length <= 10^5
# •	1 <= t.length <= 10^5
# •	s and t consist of uppercase and lowercase English letters only
# •	Expected time complexity: O(|s| + |t|)

# Open Test Cases (Visible to Candidate)
# Input:  s = "ADOBECODEBANC",  t = "ABC"
# Output: "BANC"
 
# Input:  s = "a",  t = "a"
# Output: "a"

# Solution

from collections import Counter

def minWindowSubstring(s,t):
    reqm = Counter(t)
    slidingWindow = {}

    want = 0
    required = len(reqm)

    l = 0
    min_len = float("inf")

    result = ""

    for r in range(len(s)):
        ch = s[r]
        slidingWindow[ch] = slidingWindow.get(ch,0) + 1

        if ch in reqm and slidingWindow[ch] == reqm[ch]:
            want +=1
        
        while required == want:
            if r - l +1 < min_len:
                min_len  = r - l + 1 
                result = s[l:r+1]

            left = s[l]
            slidingWindow[left] -= 1

            if left in reqm and slidingWindow[left] < reqm[left]:
                want -= 1
            
            l +=1
    
    return result

s = input("Enter value of s: ")
t = input("Enter value of t: ")

print(minWindowSubstring(s,t))
