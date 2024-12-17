import random

lst1 = []
for i in range(10):
    lst1.append(random.randint(1, 100))
print(lst1)
list1 = []
for i in lst1:
    if i % 2 != 0:
        list1.append(i)
print(list1)
list2 = []
for i in lst1:
    if i % 2 == 0:
        list2.append(i)
print(list2)
