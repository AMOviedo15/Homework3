# Aaron Oviedo 1990958

list = input().split()
numlist = []

for number in list:
    number = int(number)
    if number >= 0:
        numlist.append(number)

numlist.sort()
for number in numlist:
    print(number, end = ' ')
