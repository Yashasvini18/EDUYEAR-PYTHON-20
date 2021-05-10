input_list=[76,44,54,23,90,66,73,89,35,90,67,34,22,54]
min_value=input_list[0]
max_value=input_list[0]
for i in range(len(input_list)):
    if input_list[i]<min_value:
        min_value=input_list[i]
    if input_list[i]>max_value:
        max_value=input_list[i]
print("Minimum value from the list: ",min_value)
print("Maximum value from the list: ",max_value)
