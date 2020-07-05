# # Write a Python class to find the three elements that sum to zero
# # from a list of n real numbers.
# # Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# # Output : [[-10, 2, 8], [-7, -3, 10]]
# input=[-25, -10, -7, -3, 2, 4, 8, 10]
# li=[]
# lis=[]
# for i in range(len(input)):
#         for a in input:
#             for b in input:
#                 for c in input:
#                     if a+b+c==0 and len(li)!=3:
#                         input.remove(a)
#                         input.remove(b)
#                         input.remove(c)
#                         li.append(a)
#                         li.append(b)
#                         li.append(c)
#                     if len(li)==3 and a+b+c==0:
#                         lis.append(a)
#                         lis.append(b)
#                         lis.append(c)
# print(list(set(li)))
# print(list(set(lis)))
'''class sumzero:
    def sum(self,input):
        n=len(input)
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if input[i]+input[j]+input[k]==0:
                        print(input[i],input[j],input[k])
print(sumzero().sum([-25, -10, -7, -3, 2, 4, 8, 10]))'''
import itertools
class zero:
    def sumz(self,input):
        print([i for i in list(itertools.combinations(input,3)) if sum(i)==0])
zero().sumz([-25, -10, -7, -3, 2, 4, 8, 10])
        