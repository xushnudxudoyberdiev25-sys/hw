def rearrange_by_frequency(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda x: (-nums.count(x), x))


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))