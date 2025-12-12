fruits=['자몽','멜론','레몬']
print(fruits)
del fruits[0]
print(fruits)

nums=[1,3]
nums[1]=2
nums.append(3)
nums.append(4)
print(nums)

nums1=[1,2,3,4,5]
print(nums1[2])
#3
print(nums1[-3])
#3
print(nums1[0:3])
#123
print(nums1[2:5])
#345

nums2=[1,1,1,2,2,3,1,1,1,5,6,7,8,0,4,1,9,9,6,2,3]
print(nums2.count(1))
#3
nums2.sort()
print(nums2)


