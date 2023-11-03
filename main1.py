#sorting numbers numerically
f = open("three_digit_numbers.txt")
sample = f.read()
nums = (sample.split())
sorted_numbers = sorted(nums)
print(sorted_numbers)