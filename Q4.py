list1=["Hello","take"]
list2=["Dear","Sir"]
res=[]
for i in range(0,len(list1)):
    for n in range(0,len(list2)):
        res.append(list1[i]+' '+list2[n])

print(res)