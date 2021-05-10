input_list=[76,44,54,23,90,66,73,89,34,90,67,34]
count_even=0
count_odd=0
for i in input_list:
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("Total even numbers in the list are: ",count_even)
print("Total odd numbers in the list are: ",count_odd)
