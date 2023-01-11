def searchRange(nums, target):
    return nums[left_bound(nums, target): right_bound(nums, target) + 1]

def left_bound(nums, target):
    left = 0
    right = len(nums) - 1
    # 搜索区间为 [left, right]
    while left <= right:
        mid = left + (right - left) // 2
        if (nums[mid] < target):
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif (nums[mid] > target):
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif (nums[mid] == target):
            # 收缩右侧边界
            right = mid - 1
    # 检查出界情况
    # if (left >= len(nums) or not nums[left] == target):
    if (left >= len(nums)):
        return -1
    return left

def right_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = left + (right - left) // 2
        if (nums[mid] < target):
            left = mid + 1
        elif (nums[mid] > target):
            right = mid - 1
        elif (nums[mid] == target):
            # 这里改成收缩左侧边界即可
            left = mid + 1
    # 这里改为检查 right 越界的情况，见下图
    if (right < 0 or nums[right] != target):
        return -1
    return right

print(left_bound([0,0,0,0,1,1,2,3,3,5,6,6,7], 9))
print(searchRange([0,0,0,0,1,1,2,3,3,5,6,6,7], 0))
print(searchRange([0,0,0,0,1,1,2,3,3,5,6,6,7], 1))

def left_insert_index(nums, target):
    left = 0
    right = len(nums) - 1
    # 搜索区间为 [left, right]
    while left <= right:
        mid = left + (right - left) // 2
        if (nums[mid] < target):
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif (nums[mid] > target):
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif (nums[mid] == target):
            # 收缩右侧边界
            right = mid - 1
    if (left >= len(nums)):
        return len(nums) - 1
    return left