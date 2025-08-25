#all possible arrangements of elements
def permute(s, answer=""):
    if len(s) == 0:
        print(answer, end=" ")
        return
    for i in range(len(s)):
        # current character
        ch = s[i]
        # Substring from start up to but not including
        left = s[:i]
        # index i+1 to the end.
        right = s[i+1:]
        # except the chosen character
        rest = left + right
        permute(rest, answer + ch)
s = "abc"
permute(s)
