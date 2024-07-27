def mean(nums):
    total=0
    for num in nums:
        total=total+num
    return total/len(nums)
# # print(mean([10,20,13,45,23]))

def mode(nums):
    max_count=(0,0)
    for num in nums:
        occur=nums.count(num)
        if occur>max_count[0]:
          max_count=(occur,num)
    return max_count[1]

# print(mode([10,20,10,10,13,45,23]))
        
def median(nums):
   nums.sort()
   if len(nums)%2!=0:
      middle_index=int((len(nums)-1)/2)
      return nums[middle_index]
   elif len(nums)%2==0:
    middle_index1=int(len(nums)/2)
    middle_index2=int(len(nums)/2)-1
    return mean(nums[middle_index1],nums[middle_index2])
print(median([10,20,10,10,13,45,23]))


