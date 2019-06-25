from typing import List, Dict, Tuple

def twoSum(nums: List[int], target: int) -> List[int]:
    # d = {}
    # for i in range(0, len(nums)):
    #     d[nums[i]] = i

    # for i in range(0, len(nums)):
    #     value = target - nums[i]
    #     if d.get(value):
    #         if i == d.get(value):
    #             continue
    #         return [i, d.get(value)]

    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d.get(target - num), i]
        d[num] = i
                                            
