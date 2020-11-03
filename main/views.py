"""Main application views"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import Q

from generators.generator import generate_new_world
from .models import User, ClubInfo

def index(request):
    """View manager office when user logged in"""
    # Authenticated users view their office
    if request.user.is_authenticated:
        # User info
        user_club = request.user.clubs.get(club_info__user_club=True)
        user_manager = user_club.manager
        players = user_club.club_players.all()

        # Construct mock email address
        mock_email = f"{user_manager.manager_info.name}@{user_club.club_info.name}.co.uk"

        # Combine and order home/away fixtures
        fixtures = user_club.home_fixtures.filter(matchday__gte=request.user.matchday).union(
            user_club.away_fixtures.filter(matchday__gte=request.user.matchday)
        )
        context = {
            "user": request.user,
            "user_club": user_club,
            "user_manager": user_manager,
            "players": players,
            "star_att": user_club.get_star_att,
            "star_def": user_club.get_star_def,
            "emails": request.user.news.all()[:10],
            "email_address": mock_email.lower().replace(" ", ""),
            "fixtures": fixtures.order_by('matchday')[:10]
        }

        return render(request, "main/office.html", context)

    # Everyone else is prompted to sign in
    return redirect("login")

def transfers(request):
    """View list of non-user players"""
    players = request.user.players.filter(
            club__club_info__user_club=False
        )
    clubs = request.user.clubs.all()
    # Check to see if query has been made before applying filters
    if 'q_name' in request.GET:
        ovr = 1 if request.GET['q_ovr'] == "" else request.GET['q_ovr']
        players = players.filter(
            Q(player_info__name__icontains=request.GET['q_name'])
            & Q(club__club_info__name__icontains=request.GET['q_club'])
            & Q(player_info__pos__icontains=request.GET['q_pos'])
            & Q(player_attr__value__lte=int(request.GET['q_val']))
            & Q(player_attr__ovr__gte=ovr)
        )
        
    context = {
        "players": reversed(list(players.order_by('player_attr__value'))),
        "clubs": clubs.filter(club_info__user_club=False),
        "user_club": clubs.get(club_info__user_club=True)
    }

    return render(request, "main/transfers.html", context)

def login_view(request):
    """Log users in"""
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("index")

        return render(request, "main/login.html", {
            "message": {
                "alert": "Invalid username and/or password.",
                "type": "danger",
            }
        })

    return render(request, "main/login.html")


def logout_view(request):
    """Log users out"""
    logout(request)
    return redirect("index")


def signup_view(request):
    """Register new users"""
    if request.method == "POST":
        username = request.POST["username"].lower()
        name = request.POST["fullname"].title()
        clubname = request.POST["clubname"].title()

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "main/signup.html", {
                "message": {
                    "alert": "Sorry, your passwords didn't match - try again.",
                    "type": "danger",
                }
            })

        # Ensure fields have been filled
        if not name or not clubname:
            return render(request, "main/signup.html", {
                "message": {
                    "alert": "Please make sure that you've entered a manager name and a club name.",
                    "type": "danger",
                }
            })

        # Ensure club name is unique
        club_list = ClubInfo.objects.all()
        if club_list.filter(name=clubname):
            return render(request, "main/signup.html", {
                "message": {
                    "alert": "Club name is invalid or already in use.",
                    "type": "danger",
                }
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # generate attributes and relationships
            generate_new_world(
                user,
                club_list.filter(user_club=False),
                manager_name=name,
                club_name=clubname
            )
        except IntegrityError:
            return render(request, "main/signup.html", {
                "message": {
                    "alert": "Username is invalid or already in use.",
                    "type": "danger",
                }
            })


        login(request, user)
        return redirect("index")

    return render(request, "main/signup.html")
