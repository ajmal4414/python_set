#3 create a dictionary from a string
str1='Luminar'
dic1={}

for letter in str1:
      dic1[letter]= dic1.get(letter,0) + 1

print(dic1)