def reverse_words(s):
    # split a string into a list of substrings based on a delimiter
    words = s.split()              # split string into list of words
    reversed_words = words[::-1]   # reverse the list
    # join a list of strings into one string, with a specified separator.
    return " ".join(reversed_words)

# Test
s = "Python is awesome"
print(reverse_words(s))   # Output: awesome is Python


# using split
text = "Python is awesome"
print(text.split())  
# Output: ['Python', 'is', 'awesome']

data = "apple,banana,mango"
print(data.split(","))  
# Output: ['apple', 'banana', 'mango']



# using join
words = ['Python', 'is', 'awesome']
print(" ".join(words))  
# Output: Python is awesome

fruits = ['apple', 'banana', 'mango']
print(",".join(fruits))  
# Output: apple,banana,mango


# 
s = "Reverse this string"
result = " ".join(s.split()[::-1])
print(result)
# Output: string this Reverse
