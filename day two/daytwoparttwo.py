#to begin we need to ensure we can access the data in our input set. 

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

#now that we have the data into key value pairs that we can check we need to check for which games are true and which are false

def check(color, num):
    # red has a maximum of 12
    # green has a max of 13
    # blue has a max of  14
    if color == 'red':
        if int(num) <= 12: #check red for less than 12
            return True
        else:
            return False
    elif color == 'green':
        if int(num) <= 13: #check green for less than 13
            return True
        else:
            return False
    elif color == 'blue':
        if int(num) <= 14: #check blue for less than 14
            return True
        else:
            return False
    else:
        return False

#finally now that we know which games are true and which games are false we can add them together to get our total.
result = []

for game_num, game_lst in games.items():
    flag = True
    for game in game_lst:
        for k, v in game.items():
            if not check(k, v):
                flag = False
                break
        if not flag:
            break
    if flag:
        result.append(int(game_num))


print(sum(result))
