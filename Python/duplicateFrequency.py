def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("banana"))

def character_frequency(s):
    frequency = {}
    for letter in s:
        frequency[letter] = frequency.get(letter, 0 ) + 1
    return frequency

print(character_frequency("racecar"))

def remove_dups(my_list):
    return list(set(my_list))

def remove_ordered_duplicates(my_list):
    seen = set()
    result = []
    for item in my_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_dups([5,7,6,6,5,6,7,0]))
print(remove_ordered_duplicates([1,2,2,2,2,6,6,6,4,3,2,1]))