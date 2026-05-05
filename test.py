from random import shuffle
a = list(range(1,22))
shuffle(a)

for n in range(4):
    for i in range(5):
        if a[5*n+i] < 10:
            print(a[5*n+i], end="  ")
        else:
            print(a[5*n+i], end=" ")
    print("")
print("  ",a[20])