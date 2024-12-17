def toh(n, src, disk, aux):
    if n == 1:
        print("Move disk 1 from source", src, " to destination", disk)
        return
    toh(n - 1, src, aux, disk)
    print("Move disk", n, "from source", src, " to destination", disk)
    toh(n - 1, aux, disk, src)


a = int(input(" "))
toh(a, 'A', 'B', 'C')
