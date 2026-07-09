from collections import defaultdict
class Solution:
  #USING FREQUENCY LIST
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            key = str(count)
            hashmap[key].append(string)
        return list(hashmap.values())

    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
      hashmap=defaultdict(list)
      for string in strs:
        key="".join(sorted(string))
        hashmap[key].append(string)
      return(list(hashmap.values()))
      
"""
Approach 1 — Brute: reuse isAnagram, O(n² × m)

For every pair of strings check if anagram using isAnagram function. 
Group them together.

Why NOT to use here:

isAnagram checks two strings → O(m)
for n strings → check every pair → O(n²) pairs
total → O(n² × m)

n=10000 strings, m=100 chars
= 10000² × 100 = 10 billion operations
completely impractical

isAnagram reuse sounds clean but wrong tool here — it's a pairwise comparison. 
Group Anagrams needs a SIGNATURE approach, not pairwise.



Approach 2:
  key = sorted string
  "eat" → "aet"
  generation: O(m log m) per string ← sorting cost
  key size: m characters

Approach 3:
  key = frequency array as string
  "eat" → "[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]"
  generation: O(m) per string ← just counting, no sorting
  key size: always 26 integers regardless of m



Approach 1: isAnagram pairwise  → O(n²×m)    O(1)    ← brute, don't use
Approach 2: sorted string key   → O(n×m logm) O(n×m)  ← good, simple code
Approach 3: frequency list key  → O(n×m)      O(n×m)  ← optimal TC

"""