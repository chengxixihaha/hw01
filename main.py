for i in range(1,10):
for k in range(1,i):
    print (end="        ")
for j in range(1,10):
        print("{}x{}={:<2d}".format(i,j,i*j),end=" ")
print(" ")
