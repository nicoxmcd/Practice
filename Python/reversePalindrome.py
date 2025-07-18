def reverse_String(s):
    return s[::-1]

print(reverse_String("strawberry"))

def reverse_Loop(s):
    result =''
    for char in s:
        result = char + result
    return result

print(reverse_Loop("blueberry"))






def palindrome(s):
    return s == s[::-1]

def palindrome_Loop(s):
    backwards = ''
    for char in s:
        backwards = char + backwards
    return backwards == s

print(palindrome("racecar"))
print(palindrome("blueberry"))
print(palindrome_Loop("hi"))