
# nums=[1,7,5,6,5,2,1,6,4,4,7,7,5]

# dic=dict()

# for i in range(0,len(nums)):
#     if nums[i] in dic:
#         dic[nums[i]]+=1
#     else:
#         dic[nums[i]]=1

# print(dic)

#------------------------------------------------------method-2----------------------------------------
nums=[1,7,5,6,5,2,1,6,4,4,7,7,5]
dic={}

for i in range(0,len(nums)):
    dic[nums[i]]=dic.get(nums[i],0)+1

print(dic)











