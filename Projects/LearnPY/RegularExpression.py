import re

stm = "Python is cool i like python ..pyThon 3.7 today is 12 Jan 2019"

print(bool(re.search("python", stm, re.I)))
print(re.findall("python", stm))
print(re.search("\d", stm))
print(re.search("[^0-9A-z]", stm)) # A-z all letters
for n in re.findall("\w*", stm):
    print(n, end=" ")
print(re.split("\s",stm))
print(re.sub("\s","-",stm))