input_str=input("Enter word in which y letter is to be counted ")
input_str_count = input_str.count('y')
if input_str_count==0:
    print("Y is not present in string")
else:
    print("The count of 'y' is", input_str_count)

