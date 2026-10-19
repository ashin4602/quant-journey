def mean(nums):
    SUM=0
    if len(nums)==0:
        return None
    else:
        for i in nums:
            SUM+=i
    print("Mean=",SUM/len(nums))
n1 = []
n = int(input("How many items? "))
for i in range(n):
    item = int(input('Enter item:'))
    n1.append(item)
print("The current list given is :",n1)
mean(n1)