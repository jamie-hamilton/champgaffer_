"""Dictionaries for initial seeding of database"""
from random import randint

nationWeights = [
    10, 2, 5, 2, 0.7,
    6, 1, 0.5, 5, 0.5,
    0.5, 5, 4, 4, 1,
    4, 5, 2, 3, 0.5,
    0.5, 0.5, 0.5
]

nations = [
    {
        "nationality": "English",
        "nat_code": "en_GB",
        "flag": "flags/eng.svg",
        "weight": 10
    },
    {
        "nationality": "Irish",
        "nat_code": "en_GB",
        "flag": "flags/ire.svg",
        "weight": 2
    },
    {
        "nationality": "Scottish",
        "nat_code": "en_GB",
        "flag": "flags/sco.svg",
        "weight": 5
    },
    {
        "nationality": "Welsh",
        "nat_code": "en_GB",
        "flag": "flags/wal.svg",
        "weight": 2
    },
    {
        "nationality": "Japanese",
        "nat_code": "ja_JP",
        "flag": "flags/jp.svg",
        "weight": 0.7
    },
    {
        "nationality": "Spanish",
        "nat_code": "es_ES",
        "flag": "flags/es.svg",
        "weight": 6
    },
    {
        "nationality": "Brazilian",
        "nat_code": "pt_BR",
        "flag": "flags/br.svg",
        "weight": 1
    },
    {
        "nationality": "Czech",
        "nat_code": "cs_CZ",
        "flag": "flags/cr.svg",
        "weight": 0.5
    },
    {
        "nationality": "German",
        "nat_code": "de_DE",
        "flag": "flags/de.svg",
        "weight": 5
    },
    {
        "nationality": "American",
        "nat_code": "en_US",
        "flag": "flags/us.svg",
        "weight": 0.5
    },
    {
        "nationality": "Mexican",
        "nat_code": "es_MX",
        "flag": "flags/mx.svg",
        "weight": 0.5
    },
    {
        "nationality": "French",
        "nat_code": "fr_FR",
        "flag": "flags/fr.svg",
        "weight": 5
    },
    {
        "nationality": "Belgian",
        "nat_code": "nl_NL",
        "flag": "flags/be.svg",
        "weight": 4
    },
    {
        "nationality": "Portuguese",
        "nat_code": "pt_PT",
        "flag": "flags/pt.svg",
        "weight": 4
    },
    {   
        "nationality": "Argentinian",
        "nat_code": "es_ES",
        "flag": "flags/arg.svg",
        "weight": 1
    },
    {
        "nationality": "Italian",
        "nat_code": "it_IT",
        "flag": "flags/it.svg",
        "weight": 4
    },
    {
        "nationality": "Dutch",
        "nat_code": "nl_NL",
        "flag": "flags/nl.svg",
        "weight": 5
    },
    {
        "nationality": "Norwegian",
        "nat_code": "no_NO",
        "flag": "flags/no.svg",
        "weight": 2
    },
    {
        "nationality": "Swedish",
        "nat_code": "sv_SE",
        "flag": "flags/sv.svg",
        "weight": 3
    },
    {
        "nationality": "Polish",
        "nat_code": "pl_PL",
        "flag": "flags/pl.svg",
        "weight": 0.5
    },
    {
        "nationality": "Turkish",
        "nat_code": "tr_TR",
        "flag": "flags/tr.svg",
        "weight": 0.5
    },
    {
        "nationality": "Ghanaian",
        "nat_code": "tw_GH",
        "flag": "flags/gh.svg",
        "weight": 0.5
    },
    {
        "nationality": "Australian",
        "nat_code": "en_NZ",
        "flag": "flags/aus.svg",
        "weight": 0.5
    }
]

teams = {
    "Merseyside Mawlers": 
        {
            "club_id": 1,
            "rank": 1,
            "primary_colour": "Crimson",
            "secondary_colour": "Gold",
            "ovr": randint(19, 20),
            "formation": "4-3-3",
            "manager_nat": "German",
            "desc": "As efficient as a German car.",
            "attendance": 0.7,
            "capacity": 54000,
            "budget": 100,
            "rival": "Lannister City"
        },
    "Lannister City":
        {
            "club_id": 2,
            "rank": 2,
            "primary_colour": "LightSkyBlue",
            "secondary_colour": "#1C2C5B",
            "ovr": randint(19, 20),
            "formation": "3-5-2",
            "manager_nat": "Spanish",
            "desc": "Owned by an oil baron, probably.",
            "attendance": 0.5,
            "capacity": 56000,
            "budget": 300,
            "rival": "North United"
        },
    "Kensington Gentlemen":
        {
            "club_id": 3,
            "rank": 3,
            "primary_colour": "RoyalBlue",
            "secondary_colour": "white",
            "ovr": randint(17, 18),
            "formation": "4-4-2",
            "manager_nat": "English",
            "desc": "Know how to play but don\'t like to get their shorts dirty.",
            "attendance": 0.6,
            "capacity": 42000,
            "budget": 200,
            "rival": "Celt Crabits"
        },
    "London Hipsters":
        {
            "club_id": 4,
            "rank": 4,
            "primary_colour": "FireBrick",
            "secondary_colour": "Azure",
            "ovr": randint(16, 17),
            "formation": "4-3-3",
            "manager_nat": "Spanish",
            "desc": "Have the latest iPhone and know all the best coffee places.",
            "attendance": 0.5,
            "capacity": 60000,
            "budget": 90,
            "rival": "West Lamb"
        },
    "Celt Crabits":
        {
            "club_id": 5,
            "rank": 5,
            "primary_colour": "white",
            "secondary_colour": "SeaGreen",
            "ovr": randint(15, 17),
            "formation": "4-4-2",
            "manager_nat": "Scottish",
            "desc": "Gie us a wee swally an haud yer wheesht.",
            "attendance": 0.7,
            "capacity": 60000,
            "budget": 50,
            "rival": "Kensington Gentlemen"
        },
    "North United":
        {
            "club_id": 6,
            "rank": 6,
            "primary_colour": "#DA291C",
            "secondary_colour": "black",
            "ovr": randint(15, 17),
            "formation": "4-5-1",
            "manager_nat": "Norwegian",
            "desc": "Used to win everything before having an existential crisis.",
            "attendance": 0.4,
            "capacity": 76000,
            "budget": 150,
            "rival": "Lannister City"
        },
    "Feral Foxes":
        {
            "club_id": 7,
            "rank": 7,
            "primary_colour": "#0053A0",
            "secondary_colour": "#FDBE11",
            "ovr": randint(14, 15),
            "formation": "4-5-1",
            "manager_nat": "Italian",
            "desc": "Were strongly linked to crisps before they rebranded and won the league that time.",
            "attendance": 0.6,
            "capacity": 32000,
            "budget": 70,
            "rival": "Brummy Howlers"
        },
    "Brummy Howlers":
        {
            "club_id": 8,
            "rank": 8,
            "primary_colour": "#FDB913",
            "secondary_colour": "black",
            "ovr": randint(12, 15),
            "formation": "4-3-3",
            "manager_nat": "Portuguese",
            "desc": "Cause a few upsets. Mostly Portuguese.",
            "attendance": 0.5,
            "capacity": 32000,
            "budget": 40,
            "rival": "Feral Foxes"
        },
    "West Lamb":
        {
            "club_id": 9,
            "rank": 9,
            "primary_colour": "#7C2C3b",
            "secondary_colour": "#2DAFE5",
            "ovr": randint(12, 15),
            "formation": "4-4-2",
            "manager_nat": "English",
            "desc": "Try to play expansive football, revert to long balls when it doesn\'t work.",
            "attendance": 0.4,
            "capacity": 60000,
            "budget": 30,
            "rival": "London Hipsters"
        },
    "North East Stripeys":
        {
            "club_id": 10,
            "rank": 10,
            "primary_colour": "black",
            "secondary_colour": "white",
            "ovr": randint(12, 14),
            "formation": "4-5-1",
            "manager_nat": "English",
            "desc": "They'd love it if they beat you.",
            "attendance": 0.6,
            "capacity": 53000,
            "budget": 20,
            "rival": "Wearside Macks"
        },
    "Yorkshire Flatcaps":
        {
            "club_id": 11,
            "rank": 11,
            "primary_colour": "white",
            "secondary_colour": "#FFCD00",
            "ovr": randint(11, 12),
            "formation": "3-5-2",
            "manager_nat": "Argentinian",
            "desc": "Ey up, we'll bring more cocker.",
            "attendance": 0.8,
            "capacity": 38000,
            "budget": 18,
            "rival": "North United"
        },
    "Norfolk Budgies":
        {
            "club_id": 12,
            "rank": 12,
            "primary_colour": "#fff200",
            "secondary_colour": "#00A650",
            "ovr": 12,
            "formation": "4-4-2",
            "manager_nat": "German",
            "desc": "Where are you? Let\'s be \'avin\' you!",
            "attendance": 0.5,
            "capacity": 27000,
            "budget": 16,
            "rival": None
        },
    "Rocky Rovers":
        {
            "club_id": 13,
            "rank": 13,
            "primary_colour": "#009EE0",
            "secondary_colour": "white",
            "ovr": randint(12, 14),
            "formation": "4-3-3",
            "manager_nat": "English",
            "desc": "We won the league once, you know.",
            "attendance": 0.5,
            "capacity": 32000,
            "budget": 10,
            "rival": "Claret Coopers"
        },
    "Sherwood Goats":
        {
            "club_id": 14,
            "rank": 14,
            "primary_colour": "white",
            "secondary_colour": "#231F20",
            "ovr": randint(9, 11),
            "formation": "4-4-2",
            "manager_nat": "Dutch",
            "desc": "Club with a proud history and an indifferent present.",
            "attendance": 0.4,
            "capacity": 34000,
            "budget": 12,
            "rival": "Boozy Brewers"
        },
    "Claret Coopers":
        {
            "club_id": 15,
            "rank": 15,
            "primary_colour": "#80BFFF",
            "secondary_colour": "Maroon",
            "ovr": randint(7, 10),
            "formation": "4-4-2",
            "manager_nat": "English",
            "desc": "Above average height. Manager won\'t stand for anything fancy.",
            "attendance": 0.4,
            "capacity": 23000,
            "budget": 10,
            "rival": "Rocky Rovers"
        },
    "Boozy Brewers":
        {
            "club_id": 16,
            "rank": 16,
            "primary_colour": "#FDE92B",
            "secondary_colour": "#231F20",
            "ovr": randint(6, 11),
            "formation": "4-5-1",
            "manager_nat": "English",
            "desc": "Love a good pint and smell faintly of marmite.",
            "attendance": 0.3,
            "capacity": 7000,
            "budget": 6,
            "rival": "Sherwood Goats"
        },
    "Wearside Macks":
        {
            "club_id": 17,
            "rank": 17,
            "primary_colour": "#EB172B",
            "secondary_colour": "#211E1E",
            "ovr": randint(4, 6),
            "formation": "4-5-1",
            "manager_nat": "English",
            "desc": "Things can only get better... Oh, wait.",
            "attendance": 0.3,
            "capacity": 49000,
            "budget": 5,
            "rival": "Yorkshire Flatcaps"
        },
    "Middlebrook Mill":
        {
            "club_id": 18,
            "rank": 18,
            "primary_colour": "white",
            "secondary_colour": "#263C7E",
            "ovr": randint(2, 5),
            "formation": "4-3-3",
            "manager_nat": "English",
            "desc": "Deeply in debt but struggling on.",
            "attendance": 0.3,
            "capacity": 29000,
            "budget": 4,
            "rival": "Seaside Satsumas"
        },
    "Seaside Satsumas":
        {
            "club_id": 19,
            "rank": 19,
            "primary_colour": "#FF5F00",
            "secondary_colour": "white",
            "ovr": randint(1, 4),
            "formation": "4-4-2",
            "manager_nat": "English",
            "desc": "The Vegas of the North but without the money or glamour.",
            "attendance": 0.2,
            "capacity": 17000,
            "budget": 3,
            "rival": "Middlebrook Mill"
        },
    "Free Agent":
        {
            "club_id": 20,
            "rank": 21,
            "primary_colour": "white",
            "secondary_colour": "black",
            "ovr": 0, # choices(attribute, free)[0]
            "formation": "10-10-10",
            "manager_nat": "English",
            "desc": "This player is available on a free.",
            "attendance": 0,
            "capacity": 0,
            "budget": 0,
            "rival": None
        },
}
