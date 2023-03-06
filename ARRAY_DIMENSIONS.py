input_str = input("Enter array dimension. e.g 3,4. m,n :")
print(input_str)

dimension = [int(x) for x in input_str.split(',')]
rowNum = dimension[0]
colNum = dimension[1]
multilist = [[ 0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col
for x in multilist:
    print(x)






