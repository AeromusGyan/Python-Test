list1 = []
for i in range(0, 10):
    num = int(input("Enter the unsorted value"))
    list1.append(num)

maxi = list1[0]
for x in list1:
    if x > maxi:
        maxi = x
print(maxi)
