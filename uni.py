n = int(input())
Eng_sub = set((map(int,input().split())))
b = int(input())
Fre_sub = set((map(int,input().split())))

Per_sub = Fre_sub|Eng_sub
count = len(Per_sub)
print(count)
