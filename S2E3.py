s = input()

palindrome = s[::-1] == s

mirror_dict = {
"A": "A",
"W": "W",
"Z": "Z",
"8": "8",
"H": "H",
"T": "T",
"O": "O",
"T": "T",
"U": "U",
"V": "V",
"W": "W",
"X": "X",
"E": "3",
"J": "L",
"S": "Z",
"Z": "S", 
"3": "E",
"L": "J",
"Z": "S",
"S": "Z",
}

mirror_s = '' 
for i in s:
    if i not in mirror_dict.keys():
        break
    mirror_s += mirror_dict[i]


mirrored = mirror_s[::-1] == s

if mirrored and palindrome:
    print(s + ' is a mirrored palindrome.')
elif mirrored:
    print(s + ' is a mirrored string.')
elif palindrome:
    print(s + ' is a palindrome.')
else:
    print(s + ' is not a palindrome')