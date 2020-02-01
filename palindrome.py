def palindrome(s):
    k = len(s) - 1
    for i in range (len(s)//2 + 1):
        if s[i] != s[k]:
            break
        k -= 1
    else:
        return (True)
    return (False)
