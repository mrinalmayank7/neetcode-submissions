from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      hashmap=defaultdict(int)
      for i,char in enumerate(s):
        hashmap[char]=hashmap[char]+1 
      
      for i,char in enumerate(t):
        hashmap[char]=hashmap[char]-1 
        #if char in s is not present/less chars in s count becomes negetive
        # if count of char in s is more, some other char will become less no need to handle
        if  hashmap[char] < 0:
          return False
      return True

    def isAnagramBrute(self, s: str, t: str) -> bool:
      if sorted(s)== sorted(t):
        return True
      else:
        return False


"""
Brute vs Optimal:
Brute: sort both strings, compare → O(n log n) time O(1) space
Optimal: HashMap count characters, compare counts → O(n) time O(1) space
Why O(1) space for optimal:
Only 26 lowercase letters possible. HashMap has at most 26 keys regardless of string length. Fixed size = O(1) space.

Core idea:
Count frequency of each character in s. Then for each character in t — decrement count. If any count goes negative → t has character s doesn't have → not anagram. If all counts zero → anagram.

Rules:
Rule A — if len(s) != len(t) → return False immediately
Rule B — count frequency of each char in s → HashMap
Rule C — for each char in t → decrement count in HashMap
Rule D — if any count < 0 → return False
Rule E — return True

HIDDEN CHECK: 
Since lengths are equal — if one character goes negative, some other character must have extra positive count. But we never need to check that — the negative catch is enough.

"""