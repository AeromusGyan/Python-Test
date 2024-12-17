"""m=int(input("enter the no"))
# n=int(input("enter the odd no"))

if m%2==0:
    print("even no")
else:
    print("odd no")"""
"""
    m = int(input("enter the 1st no"))
    n = int(input("enet the 2nd no"))
    
    if m > n:
        print("largest no", m)
    else:
        print("largest no", n)
"""

"""i=1
while(i<11):

    print(i)
    i = i + 1"""

"""n = int(input("enter the any no"))
i = 1
while i < 11:
    #print(n*i)
    print(n, "*", i, "=", n*i)
    i += 1"""

"""for i in range(5):
   # print("i =",i)
    for j in range(i+1):
        #print("j=",j+1)
        print(j+1, end=" ")
    print()
"""

for i in range(5):
    for j in range(5-i):
        # print("j=", j)
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
