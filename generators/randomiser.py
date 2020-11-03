"""Randomisers for player attributes and fixtures"""
from random import randint, choices, uniform, shuffle
from statistics import mean
from faker import Faker
from .starter import nations, teams

nation_list = nations
team_list = teams

"""Probability weightings"""
# attributes
attribute = [
    randint(1,5),
    randint(6,9),
    randint(10,12),
    randint(13, 14),
    randint(15, 16),
    randint(17, 18),
    19,
    20
]
garbage = [0.2, 0.3, 0.25, 0.15, 0.05, 0.04, 0.01, 0]
low = [0.1, 0.2, 0.25, 0.3, 0.05, 0.05, 0.04, 0.01]
lowerMid= [0.05, 0.15, 0.2, 0.4, 0.1, 0.05, 0.04, 0.01]
mid = [0.04, 0.07, 0.2, 0.2, 0.2, 0.2, 0.06, 0.03]
upperMid = [0.02, 0.05, 0.07, 0.16, 0.3, 0.2, 0.15, 0.05]
top = [0.01, 0.04, 0.05, 0.1, 0.2, 0.3, 0.2, 0.1]
elite = [0, 0.01, 0.09, 0.05, 0.15, 0.2, 0.3, 0.2]
free = [0, 0.2, 0.2, 0.25, 0.175, 0.1, 0.05, 0.025]

# nations
nationWeights = [nation['weight'] for nation in nation_list]


def punter_rating(ovr):
    """Return appropriate probability weighting list from provided club ovr"""

    if ovr >= 19:
        level = elite
    elif ovr >= 17:
        level = top
    elif ovr >= 15:
        level = upperMid
    elif ovr >= 12:
        level = mid
    elif ovr >= 10:
        level = lowerMid
    elif ovr >= 7:
        level = low
    else:
        level = garbage
    return level

def player_value(ovr, handsomeness, potential):
    """Determine player value from ovr, handsomeness and potential attributes"""

    # initial value list
    values = [
        uniform(0.1,0.2),
        uniform(0.2,0.4),
        uniform(0.4,0.5),
        uniform(0.5,0.6),
        uniform(0.6,0.8),
        uniform(0.9,1.2),
        uniform(1.3,1.5),
        uniform(1.6,2),
    ]
    value = 0
    if ovr > 18:
        value = randint(13,15) + choices(values, punter_rating(ovr))[0]
    elif ovr > 16:
        value = randint(8,12) + choices(values, punter_rating(ovr))[0]
    elif ovr > 14:
        value = randint(5,8) + choices(values, punter_rating(ovr))[0]
    elif ovr > 12:
        value = randint(3,7) + choices(values, punter_rating(ovr))[0]
    elif ovr >= 10:
        value = randint(1,3) + choices(values, punter_rating(ovr))[0]
    else:
        value = (ovr / 10) + uniform(value * 0.1, value * 0.4)
    if potential > 17:
        value += uniform(value * 0.1, value * 0.2)
    if handsomeness > 17 or handsomeness > ovr + 2:
        value += uniform(value * 0.2, value * 0.4)
    return round((value), 1)



def name_faker(nat_code):
    """Return nationality dependent fake name"""

    fake = Faker(nat_code)
    if nat_code == "ja_JP":
        name = fake.first_romanized_name() + " " + fake.last_romanized_name()
    else:
        name = fake.first_name_male() + " " + fake.last_name()
    return name

def make_player(pos):
    """Create new player for team"""

    player = dict.fromkeys(["name", "nationality", "pos"])
    nationinfo = choices(nation_list, nationWeights)[0]
    player["nationality"] = nationinfo['nationality']
    player["name"] = name_faker(nationinfo['nat_code'])
    player["pos"] = pos

    return player


def make_squad(team):
    """Create new 11-player squad for team"""
    squad = []
    # determine no. of players in each position
    formation = team["formation"].split("-")

    # call make_player for amount of players required in each position and add to squad
    gkp = make_player("GK")
    squad.append(gkp)
    # make additional goalkeepers for free agents
    if team == "Free Agent":
        for i in range(2):
            gkp = make_player("GK")
            squad.append(gkp)
    # create relevant players for team formation
    for pos in range(0, int(formation[0])):
        _def = make_player("DEF")
        squad.append(_def)
    for pos in range(0, int(formation[1])):
        _mid = make_player("MID")
        squad.append(_mid)
    for pos in range(0, int(formation[2])):
        _att = make_player("ATT")
        squad.append(_att)

    return squad

# probability weightings for player ages
ages = [
    randint(16,19),
    randint(20, 24),
    randint(24, 29),
    randint(30, 33),
    randint(34, 37),
    randint(38, 40)
]
ageWeights = [0.2, 0.3, 0.35, 0.1, 0.08, 0.02]

def make_attr(team):
    """Create player attributes"""

    pl_attr = dict.fromkeys([
        "age",
        "speed",
        "strength",
        "technique",
        "potential",
        "handsomeness",
        "ovr",
        "value"
    ])
    if team == "Free Agent":
        club_ovr = choices(attribute, free)[0]
    elif team == "USER":
        club_ovr = randint(14, 15)
    else:
        club_ovr = team_list[team]['ovr']

    pl_attr["speed"] = choices(attribute, punter_rating(club_ovr))[0]
    pl_attr["strength"] = choices(attribute, punter_rating(club_ovr))[0]
    pl_attr["technique"] = choices(attribute, punter_rating(club_ovr))[0]
    pl_attr["potential"] = choices(attribute, punter_rating(club_ovr))[0]
    pl_attr["handsomeness"] = choices(attribute, punter_rating(club_ovr))[0]
    pl_attr["ovr"] = mean([
        pl_attr['speed'],
        pl_attr['strength'],
        pl_attr['technique'],
        pl_attr['potential'],
        pl_attr['handsomeness']
    ])
    pl_attr["value"] = player_value(pl_attr['ovr'], pl_attr['handsomeness'], pl_attr['potential'])
    pl_attr["age"] = choices(ages, ageWeights)[0]

    return pl_attr

def round_robin(hat):
    """ Create a schedule for the teams in the list and return it"""
    first_meet = []
    second_meet = []
    if len(hat) % 2 == 1:
        hat = hat + [None]
    # manipulate map instead of list itself
    # takes advantage of even/odd indexes to determine home vs. away
    shuffle(hat)
    n = len(hat)
    _map = list(range(n))
    _mid = n // 2
    for i in range(n-1):
        l1 = _map[:_mid]
        l2 = _map[_mid:]
        l2.reverse()
        r1 = []
        r2 = []
        for j in range(_mid):
            t1 = hat[l1[j]]
            t2 = hat[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                r1.append((t2, t1))
                r2.append((t1, t2))
            else:
                r1.append((t1, t2))
                r2.append((t2,t1))
        first_meet.append(r1)
        second_meet.append(r2)
        # rotate list by n/2, leaving last element at the end
        _map = _map[_mid:-1] + _map[:_mid] + _map[-1:]

    # combine first and second meeting into schedule
    schedule = first_meet + second_meet

    return schedule
