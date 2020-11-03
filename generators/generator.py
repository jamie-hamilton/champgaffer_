"""Generate team, player and fixture info"""
from random import randint
from main.models import (
    User,
    Nation,
    ClubInfo,
    ManagerInfo,
    PlayerInfo,
    ClubAttr,
    Club,
    Manager,
    Player,
    PlayerAttr,
    Fixture,
    News
)
from .starter import nations, teams
from .randomiser import name_faker, make_squad, make_attr, round_robin
from .news import news_items


def populate_nations():
    """Intial database seeding - add nations info from starter.py into database"""
    for nation in nations:
        Nation.objects.create(
            nationality=nation['nationality'],
            flag=nation['flag'],
            nat_code=nation['nat_code']
        )


def populate_club_info():
    """Intial database seeding - add teams info from generators.starter into database"""
    for team in teams:
        # Create sim club and manager info inline with generators.starter data
        club = ClubInfo.objects.create(
            name=team,
            primary_colour=teams[team]['primary_colour'],
            secondary_colour=teams[team]['secondary_colour'],
            desc=teams[team]['desc'],
            capacity=teams[team]['capacity'],
        )
        manager_nat = Nation.objects.get(nationality=teams[club.name]['manager_nat'])
        ManagerInfo.objects.create(
            name=name_faker(manager_nat.nat_code),
            starter_club = club,
            nation=manager_nat
        )


def populate_player_info():
    """Initial database seeding - generate squad info"""
    for team in ClubInfo.objects.all():
        # set team rivals
        rival = teams[team.name]['rival']
        if rival:
            rival_obj = ClubInfo.objects.get(name=rival)
            team.rivals.add(rival_obj)

        # build team squad
        squad = make_squad(teams[team.name])
        for player in squad:
            PlayerInfo.objects.create(
                name=player['name'],
                nation=Nation.objects.get(nationality=player['nationality']),
                pos=player['pos'],
                starter_club=team
            )

    # build user squad
    user_squad = make_squad({"formation": "4-4-2"})
    for player in user_squad:
        PlayerInfo.objects.create(
            name=player['name'],
            nation=Nation.objects.get(nationality=player['nationality']),
            pos=player['pos'],
        )


def populate_database():
    """Call functions to populate database"""
    populate_nations()
    populate_club_info()
    populate_player_info()


def generate_sim_attributes(user, club_list):
    """Generate starting attributes for sim clubs"""
    clubs = club_list
    for club in clubs:
        # Add starting attributes for clubs
        club_attr = ClubAttr.objects.create(
            rank=teams[club.name]['rank'],
            ovr=teams[club.name]['ovr'],
            formation=teams[club.name]['formation'],
            attendance=teams[club.name]['attendance'],
            budget=teams[club.name]['budget'],
            pos=teams[club.name]['rank'],
            pos_track=teams[club.name]['rank']
        )
        # Create club relationship model
        club_obj = Club.objects.create(
            user=user,
            club_info=club,
            club_attr=club_attr
        )
        # Create manager relationship model
        Manager.objects.create(
            user=user,
            manager_info=club.starter_manager,
            club=club_obj
        )

        # Create player attributes and relationships for club players
        if club.starter_players:
            squad_num = 1
            for player in club.starter_players.all():
                random_attr = make_attr(club.name)
                player_attr = PlayerAttr(squad_num=squad_num, **random_attr)
                player_attr.save()
                Player.objects.create(
                    user=user,
                    club=club_obj,
                    player_info=player,
                    player_attr=player_attr
                )
                squad_num += 1


def generate_user_attributes(user, user_input):
    """Generate starting info and attributes for user clubs"""

    # Add starting info for user controlled club
    new_club = ClubInfo.objects.create(
            name=user_input['club_name'],
            primary_colour="#2E86C1",
            secondary_colour="#FFC300",
            desc="Can you transform these plucky underdogs into world beaters?",
            capacity=22000,
            user_club=True
        )
    
    # Add starting attributes for user club
    new_club_attr = ClubAttr.objects.create(
        ovr=randint(14, 15),
        formation="4-4'2",
        attendance=0.5,
        budget=15.0
    )

    # Create user club relationship model
    new_club_obj = Club.objects.create(
        user=user,
        club_info=new_club,
        club_attr=new_club_attr
    )

    # Create user manager and relationships
    new_manager = ManagerInfo.objects.create(
        name=user_input['manager_name'],
        starter_club = new_club,
        nation=Nation.objects.get(nationality="English"),
        user_manager=True
    )
    Manager.objects.create(
        user=user,
        manager_info=new_manager,
        club=new_club_obj
    )

    # Create player attributes and relationships for club players
    squad_num = 1
    for player in PlayerInfo.objects.filter(starter_club=None):
        random_attr = make_attr("USER")
        player_attr = PlayerAttr(squad_num=squad_num, **random_attr)
        player_attr.save()
        Player.objects.create(
            user=user,
            club=new_club_obj,
            player_info=player,
            player_attr=player_attr
        )
        squad_num += 1


def generate_user_fixtures(user):
    """Create new fixtures for given user each season"""
    user_clubs = user.clubs.filter(club_attr__rank__lte=20).order_by('club_attr__rank')

    # check previous user fixture list and delete if exists
    if user.fixtures.all():
        user.fixtures.all().delete

    # generate fixtures for top league(10 highest ranked teams)
    prem_fixtures = round_robin(list(user_clubs[:10]))
    matchday = 0

    for week in prem_fixtures:
        matchday += 1
        for fixture in week:
            Fixture.objects.create(
                user=user,
                season=user.season,
                matchday=matchday,
                home=fixture[0],
                away=fixture[1]
            )

    # generate fixtures bottom league (10 lowest ranked teams)
    champ_fixtures = round_robin(list(user_clubs[10:]))

    for week in champ_fixtures:
        matchday += 1
        for fixture in week:
            Fixture.objects.create(
                user=user,
                season=user.season,
                matchday=matchday,
                home=fixture[0],
                away=fixture[1]
            )


def generate_news_stories(user, news_id=0, player=None):
    """Retrieve specific or random news story"""
    user_manager = user.managers.get(manager_info__user_manager=True)
    user_club = user.clubs.get(club_info__user_club=True)

    # Call generators.generator.news_items function to return a dict list of stories
    news_stories = news_items({
        "user": user,
        "user_manager": user_manager,
        "user_club": user_club,
        "news_id": news_id,
        "player": player
    })

    # Save generated story or stories to database
    for story in news_stories:
        news = News(user=user, **story)
        news.save()


def generate_new_world(user, club_list, **kwargs):
    """Call functions to generate new attributes, relationships and fixtures"""
    generate_sim_attributes(user, club_list)
    generate_user_attributes(user, kwargs)
    generate_user_fixtures(user)
    generate_news_stories(user, 1)


def randomise_first_user_attributes():
    """Randomise player attributes of first user in db (dev only)"""
    user = User.objects.first()
    sim_players = user.players.filter(club__club_info__user_club=False)
    user_players = user.players.filter(club__club_info__user_club=True)

    for player in sim_players:
        club = player.club.club_info
        random_attr = make_attr(club.name)
        player_attr = player.player_attr
        for (k, v) in random_attr.items():
            setattr(player_attr, k, v)
        player_attr.save()

    for player in user_players:
        random_attr = make_attr("USER")
        player_attr = player.player_attr
        for (k, v) in random_attr.items():
            setattr(player_attr, k, v)
        player_attr.save()
