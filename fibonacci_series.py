# Enter number of terms needed                   #0,1,1,2,3,5....
num = int(input("Enter the terms"))
f = 0                                         #first element of series
s = 1                                         #second element of series
if num <= 0:
    print("The requested series is", f)
else:
    print(f, s, end=" ")
    for x in range(2, num):
        nxt = f + s
        print(nxt, end=" ")
        f = s
        s = nxt
