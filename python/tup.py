def ofa(in_list):
   result=[]
   for num in in_list:
      result.append(num-1)
      result.append(num+1)
   return tuple(result)
input1=[1,2,3,4,5]
output=ofa(input1)
print(output)
