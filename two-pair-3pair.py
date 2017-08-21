nums = [1,7,6,2,1,4,3]
sorted_num = [1, 1, 2, 3, 4, 6, 7]

target = 8

def find_pairs(nums, target):
    res = []
    nums.sort()
    if nums is None:
        return []

    else:
        for i in xrange(len(nums)-1):
            j = i + 1
            k = len(nums) - 1
            while(j<k):
                if nums[j] + nums[k] == target:
                    res.append([nums[j], nums[k]])
                    j +=1
                    k -=1
                else:
                    j +=1
                if nums[i] + nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1
                else:
                    j +=1

    return res

print find_pairs(nums, target)