lisdt=[10,20,30,40,10,20,30]
pre=[]
for i in lisdt:
    if i not in pre:
        pre.append(i)
print("the preserved way")
print(pre)
unpre=list(set(lisdt))
print("the un-preserved way")
print(unpre)
