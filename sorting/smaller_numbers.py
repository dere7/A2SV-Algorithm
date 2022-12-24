
def smallerNumbersThanCurrent(nums: [int]) -> [int]:
    '''
    for each number finds out how many numbers in the
    array are smaller than it
    '''
    smaller = []
    for num in nums:
        smaller.append(len([i for i in nums if num > i]))

    return smaller
