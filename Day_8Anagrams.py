from collections import defaultdict
def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Sorting characters ensures anagrams have the same key
        key = "".join(sorted(word))
        # adds the word to list corresponding to the key
        anagram_map[key].append(word)
    return list(anagram_map.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

