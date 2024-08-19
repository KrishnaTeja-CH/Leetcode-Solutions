class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        def sol_sort(n):
            return (count[n], -n)

        nums.sort(key = sol_sort)
        return nums