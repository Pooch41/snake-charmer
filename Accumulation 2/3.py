
nums = [[[4, 3], [12, 10]], [[8, 7], [6]], [[5, 18], [15, 7, 11]], [[9], [4]], [[24, 20, 17]], [[3], [5]]]

threes = [x for sublist in nums for num in sublist for x in num if x % 3 == 0]

for sublist in nums:
    for num in sublist:
        for x in num:

print(threes)