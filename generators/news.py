"""News story generator"""
from random import randint, choices, uniform
from .randomiser import player_value

def news_items(news_dict):
    """Returns specific or random news story, taking dictionary as an argument"""
    first_name = news_dict['user_manager'].manager_info.name.split(' ')[0]
    user_club = news_dict['user_club']

    # Set news id - random when set to None
    if news_dict['news_id']:
        news_id = news_dict['news_id']
    else:
        news_id = randint(4,19)

    # Welcome stories
    if news_id == 1:
        if news_dict['user'].current_season - news_dict['user'].season == 0:
            stories = [{
                "message_id": news_id,
                "sender": "The Chairman",
                "subject": "Welcome to the club!",
                "body": f"""Hi {first_name},
                \n\nGreat to have you on board! We're confident that you're the right man to take
                 the team forward. Anything less than a mid-table finish this season would be
                 really disappointing. As we discussed in the interview, we're happy to invest
                 - so we've allocated £{user_club.club_attr.budget}M as transfer funds.
                 Good luck!\n\nWarm Regards,\nGlenn\n"""
            },
            {
                "message_id": news_id,
                "sender": "Champgaffer Overlord",
                "subject": "The gist",
                "body": """Welcome to Champgaffer!
                Your aim is to lead your club out of the second tier and onto glory in the
                 top league. A few tips so that you can get crackin'.\n\nThis is your office.
                 Come hither for news, goings on and to monitor your squad.
                 Glenn will be irritatingly hands on throughout your management journey.\n\n
                If you want to strengthen your squad - head over to 'Transfers' and put in
                 some offers... Just a warning that players who play for much bigger clubs
                 are unlikely to be interested. Soz.\n\n
                When you're ready to play a game head to 'Matchday' select your line-up and
                 formation and hit 'Proceed'.\n\n
                'Standings' is where you can monitor who is doing what throughout the season and
                 'Stats' is where you can keep tabs on the top goalscorers in each league.
                \n\nBest of luck champ!\n"""
            }]
        else:
            stories = [{
                "message_id": news_id,
                "sender": "The Chairman",
                "subject": f"""{user_club.club_info.name}
                 {news_dict['user'].current_season} Expectations""",
                "body": None
            }]
            if user_club.club_attr.rank < 3:
                stories[0]['body'] = f"""Hi {first_name},\n\n
                Thanks yet again for working so hard to make last season a success.
                 I never doubted that you're the man for the job. Same again this time around
                 please {first_name} - we want to be challenging for that title! We're giving you
                 £{user_club.club_attr.budget}M in the transfer kitty to keep us competetive.
                \n\nStay Classy,\nGlenn\n"""
            elif user_club.club_attr.rank < 7:
                stories[0]['body'] = f"""Hi {first_name},
                \n\nWe had a good showing last time out - it looks like we're on the right track!
                 We want to make sure that we're moving forward, so we're providing
                 £{user_club.club_attr.budget}M for new players.
                \n\nKeep it real,\n\nGlenn\n"""
            elif user_club.club_attr.rank < 11:
                stories[0]['body'] = f"""Hi {first_name},
                \n\nIt's great to be in the top league isn't it?
                 We'd very much like to get comfortable here, so I want you to concentrate on
                 steadying the ship this year.
                 I've put £{user_club.club_attr.budget}M aside for transfers.
                \n\nGood luck champ,\nGlenn\n"""
            elif user_club.club_attr.rank < 16:
                stories[0]['body'] = f"""Hi {first_name},
                \n\nLast season was so-so but I think that we can do better.
                 Let's give the fans something to shout about this season and push for promotion.
                 I've put £{user_club.club_attr.budget}M into the transfer account for you to
                 play with. Let's do this!\n\nWarm Regards,\nGlenn\n"""
            else:
                stories[0]['body'] = f"""Hi {first_name},
                \n\nI think we can both agree that last season was a little disappointing.
                 We expect at least a mid-table finish this time around to keep things stable.
                 We've allocated £{user_club.club_attr.budget}M to spend on players.
                 Spend it wisely and let's get cracking!\n\nWarm Regards,\nGlenn\n"""

    # Transfer offer stories
    elif news_id < 4:
        player = news_dict['player']
        budget = user_club.club_attr.budget
        player_club = player.club.club_info

        if news_id == 3:
            stories = [{
                "message_id": news_id,
                "sender": "The Chairman",
                "subject": f"FW: Transfer Offer - {player.player_info.name}",
                "body": None,
                "player": player,
            }]
            if randint(1,2) == 1:
                stories[0]['body'] = f"""Hi {first_name},
                \n\n{player.player_info.name} isn\'t even slightly interested in coming to our club
                 - his agent basically laughed at me. Maybe aim a bit lower next time.
                \nBest,\n\nGlenn\n"""
            else:
                stories[0]['body'] = f"""Hi {first_name},\n\n
                {player.player_info.name} has politely declined to join the club.
                 {player_club.name}\'s manager said that it was a decent offer but the player is
                 quite settled where he is. I think that we\'ll have to look at other targets.
                \n\nWarm Regards,\nGlenn\n"""

        else:
            if player_club.name == "Free Agent":
                stories = [{
                    "message_id": news_id,
                    "sender": "The Chairman",
                    "subject": f"FW: Free Transfer - {player.player_info.name}",
                    "body": None,
                    "player": player
                }]

                if randint(1,2) == 1:
                    stories[0]['body'] = f"""Hi {first_name},
                    \n\nThese \'free transfers\' aren't as free as they used to be,
                     I'll tell you that for a signing on fee.\n\nAnyway, {player.player_info.name}
                     seems happy and he'll be joining up with the squad immediately. We have
                     £{budget}m left in the transfer kitty.\n\nWarm Regards,\nGlenn\n"""
                else:
                    stories[0]['body'] = f"""Hi {first_name},
                    \n\n{player.player_info.name} has accepted our offer and is on his way to the
                     club as I type.\n\nI'll trust your judgement on this one, hopefully he'll
                     add something to the squad. We have £{budget}m left in transfer funds.
                    \n\nWarm Regards,\nGlenn\n"""

            else:
                stories = [{
                    "message_id": news_id,
                    "sender": "The Chairman",
                    "subject": f"FW: Transfer Offer - {player.player_info.name}",
                    "body": None,
                    "player": player,
                    "offer": None,
                }]

                if randint(1,2) == 1:
                    stories[0]['body'] = f"""Hi {first_name},
                    \n\nOur offer for {player.player_info.name} was successful!
                     See below message from {player_club}\'s manager.
                     Our transfer budget is now £{budget}m.
                    \n\nHi Glenn\n\nWe've reviewed the offer for {player.player_info.name}
                     and think that it is fair. We're reluctant to let him go but he's keen
                     to join you - look after him.
                    \n\nBest,\n{player.club.manager.manager_info.name}\n"""
                else:
                    stories[0]['body'] = f"""Hi {first_name},
                    \n\nLooks like I'm getting my chequebook out!
                     {player.player_info.name} will be joining the squad this week. We have
                     £{budget}m left in transfer funds. Here's what {player_club}\'s manager had
                     to say:\n\nHi Glenn\n\nI'd like to keep {player.player_info.name} he's pushing
                     for the move and our chairman wants to sell so we're going to accept your
                     offer. I just hope he has a stinker when we play you!
                    \n\nBest,\n{player.club.manager.manager_info.name}\n"""

    # User player stories
    elif news_id < 12:
        random_player = choices(user_club.club_players.all())[0]
        player_stats = f"""{random_player.player_info.name}:
         Age: {random_player.player_info.name} //
         Ovr: {random_player.player_attr.ovr} //
         Value: {random_player.player_attr.value}\n"""

        if news_id < 7:
            random_club = choices(news_dict['user'].clubs.filter(club_info__id__lte=19))[0]
            random_club_manager = random_club.manager.manager_info.name
            stories = [{
                    "message_id": news_id,
                    "sender": random_club_manager,
                    "subject": f"Transfer Offer - {random_player.player_info.name}",
                    "body": None,
                    "club": random_club,
                    "player": random_player,
                    "offer": round(player_value(
                        random_player.player_attr.ovr,
                        random_player.player_attr.handsomeness,
                        random_player.player_attr.potential
                    ) * uniform(0.5,0.7),1)
            }]
        else:
            stories = [{
                "message_id": news_id,
                "sender": "The Chairman" if news_id < 10 else "Head Coach",
                "subject": random_player.player_info.name,
                "body": None,
                "player": random_player,
                "offer": None
            }]

        if news_id == 4:
            stories[0]['body'] = f"""Hi {first_name},
            \n\nI like the look of {random_player.player_info.name} and want to recruit him for
             {random_club.club_info.name}. We're a bit hard up at the minute but I've pushed the
             chairman hard and we can stretch to £{stories[0]['offer']}M. What do you think?
            \n\nRegards,\n{random_club_manager}\n\n{player_stats}\n"""

        elif news_id == 5:
            stories[0]['body'] = f"""Hi {first_name},
            \n\nWe're looking to rebuild the squad at {random_club.club_info.name} and I think that
             {random_player.player_info.name}
             would be a great addition for us. Is he available? The chairman's being generous with
             this one so we can offer up to £{stories[0]['offer']}m.\n\nThanks,
            \n{random_club_manager}\n\n{player_stats}\n"""

        elif news_id == 6:
            stories[0]['body'] = f"""Hi {first_name},
            \n\nI've been admiring {random_player.player_info.name} for a while now and would like
             to bring him to {random_club.club_info.name}. How does £{stories[0]['offer']}M sound?
            \n\nThanks,\n{random_club_manager}\n\n{player_stats}\n"""

        elif news_id == 7:
            stories[0]['body'] = f"""Hi {first_name},
            \n\n{random_player.player_info.name} has been out on the town again.
             It doesn't seem to be affecting his performances but apparently his moves are
             atrocious. Could you offer a quiet word of advice? And maybe a few dance lessons.
            \n\nWarm Regards,\nGlenn\n"""

        elif news_id == 8:
            stories[0]['body'] = f"""Hi {first_name},
            \n\n{random_player.player_info.name} has been sulking about the place recently and it's
             bringing me down. Could you see what is bothering with him? Also, have you seen my
             stapler? Morag only got me a new one on the last stationery order and its already gone
             AWOL.\n\nWarm Regards,\nGlenn\n"""

        elif news_id == 9:
            stories[0]['body'] = f"""Hi {first_name},
            \n\nThe locker room showers are dripping again and our water bill is going to be
             through the roof. {random_player.player_info.name}'s uncle is a plumber if I remember
             rightly. Could you ask him what he'd charge to have a look at it?
            \n\nWarm Regards,\nGlenn\n"""

        elif news_id == 10:
            stories[0]['body'] = f"""Hi {first_name},\n\nI've been really impressed with
             {random_player.player_info.name.split()[0]} in training this week gaffer. Did you see
             that overhead kick?! I'm not sure that it warranted the obscenity of the celebration
             though. Can't have him pulling that one in front of the family stand.
            \n\nCheers,\nDave\n"""

        elif news_id == 11:
            stories[0]['body'] = f"""Hi {first_name},\n\n
            {random_player.player_info.name.split()[0]} was struggling to keep up with today's
             training session. He's just got a new Instagram model girlfriend and I don't think
             he's getting his 8 hours sleep. You might need to ask him where his priorities lie.
            \n\nCheers,\nDave\n"""

    # Misc user stories
    elif news_id < 18:
        sender = "Secretary to the Chairman" if news_id < 15 else "Head Coach" if news_id < 16 else "The Chairman"
        stories = [{
                "message_id": news_id,
                "sender": sender,
                "subject": None,
                "body": None,
        }]

        if news_id == 12:
            stories[0]['subject'] = "Stationery"
            stories[0]['body'] = f"""Hi {first_name},\n\nGlenn's lost his stapler again.
             I'm going to put it on a darn chain around his neck if it happens again.
            \nAnyway, I'm going to do another stationery order. Would you like anything?
            \n\nBest,\nMorag\n"""

        elif news_id == 13:
            stories[0]['subject'] = "Biscuits"
            stories[0]['body'] = f"""Hi {first_name},\n\n
            I'm going to get some more biscuits in, but could we store them in your office going
             forward? Glenn can inhale an entire packet of chocolate hobnobs in a matter of minutes
             when left to his own devices.\n\nBest,\nMorag\n"""

        elif news_id == 14:
            stories[0]['subject'] = "Computer systems"
            stories[0]['body'] = f"""Hi {first_name},\n\n
            Heads up that I've got the new intranet up and running now so things should run much
             more smoothly around here. I can't believe that it took 25 years for Glenn to concede
             that computers aren't just 'a fad'. Me and Dave are smashing up the filing cabinets
             this afternoon and I'm putting on a bit of a buffet to celebrate - feel free to join.
            \n\nBest\nMorag\n"""

        elif news_id == 15:
            stories[0]['subject'] = "Today"
            stories[0]['body'] = f"""Hi {first_name},\n\n
            Heads up - I'm running a bit late for training today gaffer. I stopped off at
             Sports Direct to get some new training cones and the traffic was mental in the
             city centre. £3 for 20 cones though so swings and roundabouts. See you soon.
            \n\nCheers\nDave\n"""

        elif news_id == 16:
            stories[0]['subject'] = "Going Viral"
            stories[0]['body'] = f"""Hi {first_name},\n\n
            I've just been doing some internet research and it seems that the kids are all about
             this 'TikTok'. I think that we should make a few videos. I read that some of these
             kids are making millions. MILLIONS!\n\nI have a few ideas already. Could you come
             and install it on my phone when you get a minute please {first_name}?
            \n\nWarm Regards,\nGlenn\n"""

        elif news_id == 17:
            stories[0]['subject'] = "Building Work"
            stories[0]['body'] = f"""Hi {first_name},\n\nExcuse the noise today. We've got some
             guys in to extend the trophy cabinet. No pressure or anything (but it will need
             filling). Lol, only joking (but really, it will).\n\nWarm Regards\nGlenn\n"""

    # Misc sim club stories
    elif news_id < 20:
        random_club = choices(news_dict['user'].clubs.filter(club_info__id__lte=19))[0]
        random_club_manager = random_club.manager.manager_info.name
        stories = [{
                "message_id": news_id,
                "sender": "Head Coach" if news_id < 19 else f"""Manager of
                 {random_club.club_info.name}""",
                "subject": None,
                "body": None,
                "club": random_club
        }]
        if news_id == 18:
            stories[0]['subject'] = "Espionage"
            stories[0]['body'] = f"""Hi {first_name},\n\nI'm sure that you've heard the news about
             {random_club.club_info.name} antics, spying on their opponents. We are doing daily
             patrols around the perimeter of the training ground to keep an eye out for any
             suspicous activity. Glenn was toying with the idea of shipping in some 'trained'
             coyotes from one of his friends in Mexico, but I talked him out of it.
            \n\nCheers,\nDave\n"""
        else:
            stories[0]['subject'] = "Catch Up"
            stories[0]['body'] = f"""Hi {first_name},\n\nWe haven't been in touch much recently,
             just because we manage rival teams doesn't mean that we can't be friends. How about
             we go for a drink this weekend? I know a delightful wine bar where we won't be
             bothered by all the usual riff-raff. Say, 8pm? After Saturday's game. I promise
             not to get you too drunk and steal all of your secrets ; - )
            \n\nYours,\n{random_club_manager}\n"""

    # Board confidence update
    elif news_id == 20:
        board_confidence = news_dict['user_manager'].manager_info.board_confidence
        stories = [{
                "message_id": news_id,
                "sender": "The Chairman" if board_confidence > 50 else "Secretary to the Chairman",
                "subject": "Board Meeting",
                "body": None,
        }]
        if board_confidence > 90:
            stories[0]['body'] = f"""Hi {first_name},\n\n
            Things are going so well at the minute I could kiss you! I am such a picture of zen
             that I've even stopped getting on the wife's nerves. Keep it up buddy!
            \n\nLove you,\nGlenn\n"""
        elif board_confidence > 70:
            stories[0]['body'] = f"""Hi {first_name},\n\n
            Just a quick message to let you how the board meeting went today. We're happy with how
             things are going generally. Of course, there's always room for improvement so keep
             chipping away and let me know if I can help with anything. Keep up the hard work.
            \n\nWarm Regards,\nGlenn\n"""
        elif board_confidence > 50:
            stories[0]['body'] = f"""Hi {first_name},\n\nSome of the guys on the board have been
             raising their concerns about your leadership. I'll keep fighting your corner but we're
             going to have to string some wins together soon champ.\nBig Glenn's here if you need
             to chat.\n\nRegards,\nGlenn\n"""
        else:
            stories[0]['body'] = f"""Hi {first_name},\n\nGlenn was sobbing into a pile of hobnobs
             after the board meeting today. I don't think that you'll be getting a message from
             him but I think you should know that it didn't go well. We need to win some matches
             {first_name}. Do you want me to take training this week? You look like you need a
             break & to be honest, I think I'd do a better job.\n\nBest,\nMorag\n"""

    # End of season stories
    elif news_id == 21:
        clubs_by_pos = news_dict['user'].clubs.filter(club_attr__rank__lte=20).order_by('club_attr__pos')
        champions = clubs_by_pos[0]
        relegated = clubs_by_pos[8:10]
        promoted = clubs_by_pos[10]
        runner_up = clubs_by_pos[11]
        stories = [{
                "message_id": news_id,
                "sender": "Football Round Up",
                "subject": f"{champions.club_info.name} are champions!",
                "body": f"""{champions.club_info.name} have been crowned the champions of English
                 football after a hard fought season. The celebrations went on into the wee hours
                 of the morning for {champions.manager.manager_info.name}'s team.\n\n
                There was less to cheer about for {relegated[0].club_info.name} and
                 {relegated[1].club_info.name}, as both clubs were relegated from the top league
                 and will have to battle it out in the second tier next season.\n""",
                "club": champions
            },
            {
                "message_id": news_id,
                "sender": "Football Round Up",
                "subject": f"{promoted.club_info.name} clinch the title",
                "body": f"""{promoted.club_info.name} will be mixing it with the big boys next
                 season after finishing the season at the summit of the second tier.
                \n\n{runner_up.club_info.name} ran them close and won't be too disappointed,
                 as their 2nd place finish means that they'll join {promoted.club_info.name} at
                 the top table of English Football.\n""",
                "club": promoted
            }]
        if champions == user_club:
            stories.append({
                "message_id": news_id,
                "sender": "The Chairman",
                "subject": "We are the champions my friend!",
                "body": f"""I don't bloody believe it {first_name}! I have dreamt of this day but
                 never thought it would come. Thank you so much!!!\n\nGet to my office ASAP -
                 Morag's cracking out the champers.\n\nI love you, always,\n\nGlenn\n""",
                "club": user_club
            })

    return stories