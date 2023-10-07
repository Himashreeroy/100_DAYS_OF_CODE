from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}  # Dictionary to store groups of anagrams
        
        for word in strs:
            # Sort the word to create a key for the anagrams dictionary
            sorted_word = ''.join(sorted(word))
            # If the key exists, add the word to the corresponding group, otherwise create a new group
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        # Return the values of the dictionary as the grouped anagrams
        return list(anagrams.values())

# Example usage
sol = Solution()
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]

print(sol.groupAnagrams(strs1))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

print(sol.groupAnagrams(strs2))
# Output: [['']]

print(sol.groupAnagrams(strs3))
# Output: [['a']]

        