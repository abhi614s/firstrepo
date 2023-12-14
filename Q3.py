# Input: abcefghijklm
# target = 4
# Output: ebca ihgf mlkj

input_str = "abcdefghijkl"
target = 4
new_str = ""

start = 0
for i in range(0,len(input_str)):
    if ((i+1)%target==0):
        new_str += input_str[i:start:-1]
        start = i

final_str = new_str[:target-1] + input_str[0] + new_str[target-1:]

print(final_str)
