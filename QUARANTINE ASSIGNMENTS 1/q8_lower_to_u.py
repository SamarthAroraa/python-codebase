def toupper(s):
    ans=""
    for m in s:
        if(ord(m)<123 and ord(m)>=97):
            m= chr(ord(m)-32)
        ans+=m
    return ans
string = input("Enter a string:")
print("Modified toupper string:", toupper(string))
