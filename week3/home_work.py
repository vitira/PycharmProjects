#Count how many fifth you have in the list

nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
count = 0
for num in nums:
    if num == 5:
        count = count+1
print(count)

print("_______________________________________________")

mynum  = int(input("Enter a number: "))
if mynum % 3 ==0 and mynum %5 ==0:
    print("FuzzBuzz")
elif mynum % 5 ==0:
    print("Buzz")
elif mynum % 3 ==0:
    print("Fuzz")
else:
    print("Wrong number")

