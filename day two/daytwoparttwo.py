#to begin part two we need to ensure we can access the data in our input set.
with open("daytwoinput.txt") as d:
    info = d.readlines()

#next we need to turn out data set into a dictionary with 1-1 key value pairs, we have the beginnign set up as game one is set up in the follwoing
    #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

games = {}
for game in info:
    key_part, value_part = game.rstrip("\n").split(':')
    key = key_part.split(' ')[1]
    value_list = value_part.split(';')
    value = []
    for v in value_list:
        v = v.split(',')
        v_dict = {}
        for ele in v:
            num, color = ele.split(' ')[1:]
            v_dict[color] = num
        value.append(v_dict)
    games[key] = value
print(games)

# now we need to get the power by initializing each color as the number one
def get_power(lst):
    red = 1
    green = 1
    blue = 1
    for game in lst:
        for color, num in game.items():
            if color == "red":
                if int(num) >= red:
                    red = int(num)
            elif color == "green":
                if int(num) >= green:
                    green = int(num)
            else:
                if int(num) >= blue:
                    blue = int(num)
    return red*green*blue

result = 0
for game in games:
    result += get_power(games[game])

print(result)

