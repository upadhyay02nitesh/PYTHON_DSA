s="aruwiy1u2h3lilh h345d bdkgou43"
v=""
c=""

vowel=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i.isalpha():
        if i in vowel:
            v=v+i
        else:
            c=c+i 
print("Vowels :",v)
print("Consonent :",c)


d=""
space=0
for i in s:
    if i.isdigit():
        d+=i 
    elif i.isspace():
        space+=1 
print("Digit : ",d)
print("Spaces :",space)
