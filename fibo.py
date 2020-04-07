n=int(input("Upto how many numbers u wanna input :"))
f=0
s=1
if n==1:
    print(0)
elif n==2:
    print(0,1)
elif n>2:
    print(0,1,end=" ")
    for x in range(n-2):
        sum=f+s
        print(sum,end=" ")
        f=s
        s=sum
else:
        print('invalid input')
