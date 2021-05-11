input_str = "abed"
result = []
for ele in range(len(input_str)):
    if input_str[ele] in "aeiou":
       result.append(ele)
print(str(result)) 
