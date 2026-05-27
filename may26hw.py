# Find second max number from the list
"""list=[34,87,73,55,84,21,49]
list.sort()
print(list[-2])"""

#Find second min number from the list
"""list=[34,87,73,55,84,21,49]
list.sort()
print(list[1])"""

l1=[111,1234,11,1234,4567,67,5678]
count=0
for number in l1:
    if str(number)[0]=="1":
        count=count+1
print("Total number starting with 1 are",count)

