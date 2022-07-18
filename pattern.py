a="SSSSSSSS"
print(a)
for x in range(8):
    print("S")
print(a)
for x in range(8):
    for y in range(8):
        if (y==7):
            print("S")
        else:
            print(" ",end='')
print(a)