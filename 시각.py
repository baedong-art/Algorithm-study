h = int(input())

count = 0

#ex) 03시20분35초 ->032035
for i in range(h+1):
    for j in range(60): #분
        for k in range(60):#초
            if '3' in str(i) +str(j)+ str(k):
                count += 1
print(count)
