def longCommonPrefix(strs):
           # If there is no common prefix, return an empty string
    
    if not strs:
        return ""
    
    prefix = strs[0]   # take first word
    
    for word in strs[1:]:
        while word.find(prefix) != 0:   # check if prefix matches
            prefix = prefix[:-1]     # shrink prefix
            if not prefix:
                return ""
    return prefix
strs = ["flower", "flow", "flight"]
print(longCommonPrefix(strs))   
# The prefix must be at the beginning of each string.