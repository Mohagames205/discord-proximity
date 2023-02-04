import numpy as np

players =  {"Mohamed": 20, "Rik": 10, "Jan": 15, "John": 35, "Peter": 40, "Karel": 50, "Dieter": 60}
distance_limit = 10

def distance(x1, x2):
    return abs(x1 - x2)


def check_relations(name, blacklist=None, result=None):
    """
    Default arguments in Python are evaluated only once, when the function is defined. 
    When the function is subsequently called, the same objects are used as default arguments, rather than being re-created.
    """
    if blacklist == None or result == None:
        blacklist = []
        result = {}

    position = players[name]
    exclusion_list = players.copy()

    if name not in blacklist:
        blacklist.append(name)

    for user in blacklist:
        exclusion_list.pop(user)
    
    for player_name, coordinate in exclusion_list.items():
        if distance(coordinate, position) <= 10:
            result[player_name] = coordinate
            check_relations(player_name, blacklist, result)

    return result


for name, _ in players.items():
    print(name, check_relations(name))




