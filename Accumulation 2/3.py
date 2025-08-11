
nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]

threes = [num for sublist in nums for num in sublist if num % 3 == 0]