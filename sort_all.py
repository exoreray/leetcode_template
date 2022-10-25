# https://leetcode.cn/problems/sort-an-array/solutions/1758002/by-itcharge-vsel/
import random

class Solution:


    def bubbleSort(self, arr):
        # 第 i 趟排序
        for i in range(len(arr)):
            # 从序列中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较
            for j in range(len(arr) - i - 1):
                # 相邻两个元素进行比较，如果前者大于后者，则交换位置
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


    def selectionSort(self, arr):
        for i in range(len(arr) - 1):
            # 记录未排序部分中最小值的位置
            min_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                arr[i], arr[min_i] = arr[min_i], arr[i]
        return arr


    def insertionSort(self, arr):
        # 遍历无序序列
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            # 从右至左遍历有序序列
            while j > 0 and arr[j - 1] > temp:
                # 将有序序列中插入位置右侧的元素依次右移一位
                arr[j] = arr[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            arr[j] = temp

        return arr


    def shellSort(self, arr):
        size = len(arr)
        gap = size // 2
		# 按照 gap 分组
        while gap > 0:
            # 对每组元素进行插入排序
            for i in range(gap, size):
                # temp 为每组中无序序列第 1 个元素
                temp = arr[i]
                j = i
                # 从右至左遍历每组中的有序序列元素
                while j >= gap and arr[j - gap] > temp:
                    # 将每组有序序列中插入位置右侧的元素依次在组中右移一位
                    arr[j] = arr[j - gap]
                    j -= gap
                # 将该元素插入到适当位置
                arr[j] = temp
            # 缩小 gap 间隔
            gap = gap // 2
        return arr


    def mergeSort(self, arr):                       # 分割过程

        def merge(left_arr, right_arr):           # 归并过程
            arr = []
            left_i, right_i = 0, 0
            while left_i < len(left_arr) and right_i < len(right_arr):
                # 将两个有序子序列中较小元素依次插入到结果数组中
                if left_arr[left_i] < right_arr[right_i]:
                    arr.append(left_arr[left_i])
                    left_i += 1
                else:
                    arr.append(right_arr[right_i])
                    right_i += 1
            
            while left_i < len(left_arr):
                # 如果左子序列有剩余元素，则将其插入到结果数组中
                arr.append(left_arr[left_i])
                left_i += 1
                
            while right_i < len(right_arr):
                # 如果右子序列有剩余元素，则将其插入到结果数组中
                arr.append(right_arr[right_i])
                right_i += 1
            
            return arr                                  # 返回排好序的结果数组


        if len(arr) <= 1:                           # 数组元素个数小于等于 1 时，直接返回原数组
            return arr
        
        mid = len(arr) // 2                         # 将数组从中间位置分为左右两个数组。
        left_arr = self.mergeSort(arr[0: mid])      # 递归将左子序列进行分割和排序
        right_arr =  self.mergeSort(arr[mid:])      # 递归将右子序列进行分割和排序
        return merge(left_arr, right_arr)      # 把当前序列组中有序子序列逐层向上，进行两两合并。


    def quickSort(self, arr, low, high):

            # 从 arr[low: high + 1] 中随机挑选一个基准数，并进行移动排序
        def randomPartition(arr, low: int, high: int):

            # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
            def partition(arr, low: int, high: int):
                pivot = arr[low]            # 以第 1 为为基准数
                i = low + 1                 # 从基准数后 1 位开始遍历，保证位置 i 之前的元素都小于基准数
                
                for j in range(i, high + 1):
                    # 发现一个小于基准数的元素
                    if arr[j] < pivot:
                        # 将小于基准数的元素 arr[j] 与当前 arr[i] 进行换位，保证位置 i 之前的元素都小于基准数
                        arr[i], arr[j] = arr[j], arr[i]
                        # i 之前的元素都小于基准数，所以 i 向右移动一位
                        i += 1
                # 将基准节点放到正确位置上
                arr[i - 1], arr[low] = arr[low], arr[i - 1]
                # 返回基准数位置
                return i - 1

            # 随机挑选一个基准数
            i = random.randint(low, high)
            # 将基准数与最低位互换
            arr[i], arr[low] = arr[low], arr[i]
            # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
            return partition(arr, low, high)


        if low < high:
            # 按照基准数的位置，将序列划分为左右两个子序列
            pi = randomPartition(arr, low, high)
            # 对左右两个子序列分别进行递归快速排序
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

        return arr



    # 调整为大顶堆
    def heapify(self, arr, index, end):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子节点
            max_index = index
            if arr[left] > arr[max_index]:
                max_index = left
            if right <= end and arr[right] > arr[max_index]:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            arr[index], arr[max_index] = arr[max_index], arr[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 初始化大顶堆
    def buildMaxHeap(self, arr):
        size = len(arr)
        # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((size - 2) // 2, -1, -1):
            self.heapify(arr, i, size - 1)
        return arr


    # 升序堆排序，思路如下：
    # 1. 先建立大顶堆
    # 2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值
    # 3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值
    # 4. 以此类推，直到最后一个元素交换之后完毕。
    def maxHeapSort(self, arr):
        self.buildMaxHeap(arr)
        size = len(arr)
        for i in range(size):
            arr[0], arr[size-i-1] = arr[size-i-1], arr[0]
            self.heapify(arr, 0, size-i-2)
        return arr


    def countingSort(self, arr):
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr_min, arr_max = min(arr), max(arr)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = arr_max - arr_min + 1
        counts = [0 for _ in range(size)]
        
        # 统计值为 num 的元素出现的次数
        for num in arr:
            counts[num - arr_min] += 1
        
        # 计算元素排名
        for j in range(1, size):
            counts[j] += counts[j - 1]

        # 反向填充目标数组
        res = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            # 根据排名，将 arr[i] 放在数组对应位置
            res[counts[arr[i] - arr_min] - 1] = arr[i]
            # 将 arr[i] 的对应排名减 1
            counts[arr[i] - arr_min] -= 1

        return res


    def insertionSort(self, arr):
        # 遍历无序序列
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            # 从右至左遍历有序序列
            while j > 0 and arr[j - 1] > temp:
                # 将有序序列中插入位置右侧的元素依次右移一位
                arr[j] = arr[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            arr[j] = temp

        return arr


    def bucketSort(self, arr, bucket_size=5):
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr_min, arr_max = min(arr), max(arr)
        # 定义桶的个数为 (最大值元素 - 最小值元素) // 每个桶的大小 + 1
        bucket_count = (arr_max - arr_min) // bucket_size + 1
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历原始数组元素，将每个元素装入对应区间的桶中
        for num in arr:
            buckets[(num - arr_min) // bucket_size].append(num)

        # 对每个桶内的元素单独排序，并合并到 res 数组中
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)

        return res


    def radixSort(self, arr):
        # 桶的大小为所有元素的最大位数
        size = len(str(max(arr)))

        # 从低位到高位依次遍历每一位，以各个数位值为索引，对数组进行按数位排序
        for i in range(size):
            # 使用一个长度为 10 的桶来存放各个位上的元素
            buckets = [[] for _ in range(10)]
            # 遍历数组元素，根据元素对应位上的值，将其存入对应位的桶中
            for num in arr:
                buckets[num // (10 ** i) % 10].append(num)
            # 清空原始数组
            arr.clear()
            # 从桶中依次取出对应元素，并重新加入到原始数组
            for bucket in buckets:
                for num in bucket:
                    arr.append(num)

        return arr