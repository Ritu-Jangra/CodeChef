# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    num=map(int,input().strip().split())
    pos=0
    neg=0
    
    for i in num:
        if i < 0 :
            neg+=1
        else:
            pos+=1
    if pos==0 or neg==0:
        print(pos,pos)
    else:
        if neg>pos:
            print(neg,pos)
        else:
            print(pos,neg)
