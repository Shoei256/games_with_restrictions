from numpy import ceil
dic={}
def move(x,y):
    t=(x,y)
    if t in dic:
        return dic[t]
    w=ceil((x+2*y)/2)
    flag=False
    for a in range(x+1):
        for b in range(y+1):
            if a==b==0:
                continue
            if a+b*2<=w:
                flag|=move(x-a,y-b)
    flag= not flag
    dic[t]=flag
    return flag
move(60,60)
p=[]
for i in dic:
    if dic[i]:
        p.append(i)
print(sorted(p))