nums = [10, 25, 30, 2, 45, 18, 7]
target = 20
# Saída esperada: [0, 1]

def two_sum(nums, target):
    caderno = {}
    for i in range(len(nums)):
        if nums[i] in caderno:
            return [caderno[nums[i]], i]
        else:
            caderno[target - nums[i]] = i
print(two_sum(nums, target))