input_list=[1,2,3,3,2,4]
output=[]
for i in input_list:
    if i not in output:
        output.append(i)
print(output)
