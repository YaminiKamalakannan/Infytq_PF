flag=0
year=int(input())
if year%4==0:
    if year%100!=0:
        flag=1
elif year%400==0:
       flag=1
print(flag)
