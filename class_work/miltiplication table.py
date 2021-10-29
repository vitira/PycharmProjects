### multiplication table

for x in range(1, 11):
    for y in range(1, 11):
        #print(y)
        print(x*y, end = "\t")
    print()

#############anothe multiplication
nums1 = range(1,11)
nums2 = range(1,11)
for row in nums1:
    for col in nums2:
        print(f"{col}*{row}={row*col}", end='\t')
    print()