import re

str1= "H e l l o"
a=r'[aeiouAEIOU]'
vowel= re.findall(a,str1)
print(" ",str1.upper())
print(" ",str1.lower())
print(" ",len(vowel))

