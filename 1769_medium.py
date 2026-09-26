boxes = "110"

new = []

l = len(boxes)
for i in range (0,l):
    sum = 0
    s = 0
    for j in range (0,l):
        if (i==j):
            continue
        if (boxes[j]=="1"):
            s=j-i
            if (s<0):
                s*=-1
            sum += s       
    new.append(sum)

for i in range (0,l):
    print(new[i])