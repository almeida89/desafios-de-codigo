'''
01 - Two Sum

Dado o array de inteiros *nums* e um inteiro *target*, retorne os indices dos dois números
de forma que a soma deles seja *target*
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_map:
                return [seen_map[complement], i]
            seen_map[num] = i
        return

if __name__ == "__main__":
    sol = Solution()
    
    # Exemplo 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Entrada: nums={nums1}, target={target1}")
    print(f"Saída: {sol.twoSum(nums1, target1)}") # Saída: [0, 1] (pois nums[0] + nums[1] == 9)
    print("-" * 20)