number_word = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

#we need to itentify word digit pairs so that we can find and replace
#the words with digits to find the correct first and last digit for the values

#first we need to import our data so that we can read it.
with open("inputpuzzleone.txt") as values:
    data = values.readlines()

#print(data) check to make sure code works to solve bugs early

    #this will instruct the program to read the data line by line so we can
    #correctly identify first and last of the line.
          

#just like in the first part we need to remove the \n
str_list = []
for string in data:
    new_str = string.rstrip("\n")
    str_list.append(new_str)
# now we need to create a function to find the first actual number in the set. This is different than
#in the first part as we have assigned key value pairs. we need to use the key portion 

def first_number(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]
        else:
            for key in number_word:
                if string[i:].startswith(key):
                    return number_word[key]


def last_number(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i].isdigit():
            return string[i]
        else:
            for key in number_word:
                if string[:i+1].endswith(key):
                    return number_word[key]


def get_num(string):
    first = first_number(string)
    last = last_number(string)
    # print(first)
    # print(last)
    return int(first + last)



total = 0
for string in str_list:
    print(string)
    num = get_num(string)
    total += num

print(total)
