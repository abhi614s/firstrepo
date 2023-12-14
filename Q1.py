# Input: "this is a new day at brudite"
# Output: "ThiS IS A NeW DaY AT BruditE"

str = "this is a new day at brudite"
list = list(str)

list[0] = list[0].upper()
list[-1] = list[-1].upper()

for i in range(1,len(list)):
    # print(list[i])
    if ((list[i] == ' ') and (list[i-1] != ' ')):
        list[i-1] = list[i-1].upper()
    
    if ((list[i] != ' ') and (list[i-1] == ' ')):
        list[i] = list[i].upper()

new_str = ''.join(list)

print(new_str)
