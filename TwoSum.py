# def twoSum(nums: list[int], target: int) -> list[int]:
#     '''Returns the two list indecies of element's which summed value equals the target.'''
#     for i in nums:
#         print(i)
#         for x in nums[nums.index(i) + 1:]:
#             print(x)
#             if i + x == target:
#                 indexList = []
#                 indexList.append(nums.index(i))
#                 indexList.append(nums.index(x))
#                 # The following line assumes that there will always be a solution
#                 return indexList

# nums = [3,3]
# target = 6
# print(twoSum(nums, target))

def twoSum(nums: list[int], target: int) -> list[int]:
    '''Returns the two list indecies of element's which summed value equals the target.'''
    for i in range(len(nums)):
        print(nums[i])
        for x in range(i + 1,len(nums)):
            print(nums[x])
            if nums[i] + nums[x] == target:
                indexList = []
                indexList.append(i)
                indexList.append(x)
                # The following line assumes that there will always be a solution
                return indexList

nums = [2,7,11,15]
target = 17
print(twoSum(nums, target))