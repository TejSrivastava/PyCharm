list=[1,2,3,4,5]
count=0
k=int(input('Enter the value of k: '))
for x in list:
    for y in list:
        diff=abs(x-y)

        if(diff==k):
            count=count+1
print(f"{count} pairs of integers has {k} as a difference")

