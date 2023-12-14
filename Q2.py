# Input: aaabbccaab
# Output: a3b2c2a2b

input_str = "aaabbccaab"
new_str = ""
count = 1

for i in range(0,len(input_str)):
    
    if(i < len(input_str) - 1):
        if((input_str[i] == input_str[i+1])):
            count = count + 1
        else:
            new_str += input_str[i]
            new_str += str(count)
            count = 1
    else:
        new_str += input_str[i]
        new_str += str(count)

for i in range(0,len(new_str)):
    print(new_str[i], end='')
