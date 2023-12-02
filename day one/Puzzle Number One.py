import re
#first we need to import the input valuse in order to work with them.
with open("inputpuzzleone.txt") as values:
    data = values.readlines() #this will read each line, line by line.

#we need to move the data into a list containting strings, so that we can remove
#what we dont need, and assess just the beginning and the end number.

str_list = []
for string in data:
    new_str = string.rstrip("\n")
    str_list.append(new_str)
#print(str_list) test to see if the above has worked to ensure their are not any bugs

#next we need to find the first number from index 0 in our list as well as teh
#2nd number from index of -1. then we need to put them together to create our numbe
# then add all the numbers together to create our sum total for out calibration values

def get_number(string):
    numbers = re.findall(r'\d+', string)
    first = numbers[0][0]
    second = numbers[-1][-1]
    num = int(first + second)
    return num

#to add all the num together to get our calibration value

total = 0
for string in str_list:
    num = get_number(string)
    total += num

print(total)


    

