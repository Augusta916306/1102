#solution to analyze a text file
f = open("three_digit_numbers.txt") 
sorted_numbers = f.read()
sample = "380 339 420 308 448"

cols = sample.split()
num_list = []
for col in cols:
    num = int(col)
    num_list.append(num)
start = min(num_list)
for count in range(start, max(num_list)):
    #print(count)
   # if count in num_list:
    #we have a membership
         #pass
# else:
    #otherwise
    if count not in num_list:
        print(f"{count}, is missing")