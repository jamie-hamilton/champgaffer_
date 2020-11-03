"""Champgaffer data models"""

import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """User model"""
    matchday = models.IntegerField(default=1)
    season = models.IntegerField(default=datetime.date.today().year)
    current_season = models.IntegerField(default=datetime.date.today().year)

    def __str__(self):
        """Return object string."""
        return f'{self.username}'


class ManagerInfo(models.Model):
    """Manager info model"""
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=40)
    board_confidence = models.IntegerField(default=40)
    nation = models.ForeignKey(
        "Nation",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    starter_club = models.OneToOneField(
        "ClubInfo",
        related_name="starter_manager",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user_manager = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """Return object string."""
        return f'{self.name}'
    
    def avatar_url(self):
        """Return url to manager avatar"""
        return f"https://avatars.dicebear.com/v2/male/{self.name}.svg"


class Manager(models.Model):
    """Manager relationship manager"""
    user = models.ForeignKey(
        User,
        related_name="managers",
        on_delete=models.CASCADE,
    )
    manager_info = models.OneToOneField(
        ManagerInfo,
        on_delete=models.CASCADE,
    )
    club = models.OneToOneField(
        "Club",
        related_name="manager",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return object string."""
        return f'{self.manager_info.name}'


class ClubInfo(models.Model):
    """Club info model"""
    name = models.CharField(
       unique=True,
       max_length=50,
       help_text='Enter your team name.',
    )
    primary_colour = models.CharField(
       max_length=25,
       help_text='Enter primary team colour (RGB, RGBA or HEX).',
       default="#2E86C1",
    )
    secondary_colour = models.CharField(
       max_length=25,
       help_text='Enter secondary team colour (RGB, RGBA or HEX).',
       default="#FFC300",
    )
    desc = models.TextField(
       max_length = 100,
       default = "Can you transform these plucky underdogs into world beaters?",
    )
    capacity = models.IntegerField(
       default=22000,
    )
    rivals = models.ManyToManyField("ClubInfo", blank=True, default=12)
    user_club = models.BooleanField(
        default=False,
    )

    def __str__(self):
        """Return object string."""
        return f"{self.name}"


class ClubAttr(models.Model):
    """Track club attributes"""
    rank = models.IntegerField(default=20)
    budget = models.DecimalField(decimal_places=2, default=15.00, max_digits=5)
    ovr = models.IntegerField(
        help_text="Value between 1 and 20",
    )
    formation = models.CharField(
        max_length=5,
        default="4-4-2",
    )
    attendance = models.DecimalField(decimal_places=2, default=0.5, max_digits=3)
    pld = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    ga = models.IntegerField(default=0)
    pts = models.IntegerField(default=0)
    pos = models.IntegerField(default=20)
    pos_track = models.IntegerField(default=20)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(ovr__gte=0) & models.Q(ovr__lte=20),
                name="A value between 1 and 20 is required.",
            )
        ]

    def __str__(self):
        """Return object string."""
        return "Club attributes."

    def is_top_league(self):
        """Return true if club is in top league"""
        if self.pos > 10:
            return False
        return True

    def ovr_as_percent(self):
        """Return ovr as percentage"""
        return self.ovr * 5


class Club(models.Model):
    """Club relationship manager"""
    user = models.ForeignKey(
        User,
        related_name="clubs",
        on_delete=models.CASCADE,
    )
    club_info = models.OneToOneField(
        ClubInfo,
        related_name="club",
        on_delete=models.CASCADE,
    )
    club_attr = models.OneToOneField(
        ClubAttr,
        related_name="club_instance",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return object string."""
        return f"{self.user.username} // {self.club_info.name}"

    def get_star_att(self):
        """Return club attacker with highest ovr value"""
        return self.club_players.filter(
            models.Q(player_info__pos="ATT") |
            models.Q(player_info__pos="MID")
        ).order_by('player_attr__ovr').last()

    def get_star_def(self):
        """Return club defender with highest ovr value"""
        return self.club_players.filter(
            models.Q(player_info__pos="DEF") |
            models.Q(player_info__pos="GK")
        ).order_by('player_attr__ovr').last()


class Nation(models.Model):
    """Nation model"""
    nationality = models.CharField(
       unique=True,
       max_length=20,
       help_text='Enter name of country.',
    )
    flag = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Location of svg image of nation flag.",
    )
    nat_code = models.CharField(
        max_length=5,
        help_text="Enter valid <a href='https://faker.readthedocs.io/en/master/locales.html'>faker locale code</a>."
    )

    def __str__(self):
        """Return object string."""
        return f"{self.nationality}"


class PlayerInfo(models.Model):
    """Player Info model"""
    name = models.CharField(
       max_length=100,
       help_text='Enter a player name.',
    )
    nation = models.ForeignKey(
        Nation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    pos = models.CharField(
        max_length=3,
        help_text='Enter player position',
    )
    starter_club = models.ForeignKey(
        "ClubInfo",
        related_name="starter_players",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


    def __str__(self):
        """Return object string."""
        return f"{self.name}"

    def avatar_url(self):
        """Return url to player avatar"""
        return f"https://avatars.dicebear.com/v2/male/{self.name}.svg"


class PlayerAttr(models.Model):
    """Track player attributes"""
    age = models.IntegerField()
    speed = models.DecimalField(decimal_places=2, max_digits=4)
    strength = models.DecimalField(decimal_places=2, max_digits=4)
    technique = models.DecimalField(decimal_places=2, max_digits=4)
    potential = models.DecimalField(decimal_places=2, max_digits=4)
    handsomeness = models.DecimalField(decimal_places=2, max_digits=4)
    value = models.DecimalField(decimal_places=2, max_digits=4)
    ovr = models.DecimalField(decimal_places=1, max_digits=3, null=True, blank=True)
    squad_num = models.IntegerField()

    def __str__(self):
        """Return object string."""
        return "Player attributes."

    def ovr_as_percent(self):
        """Return ovr as percentage"""
        return self.ovr * 5


class Player(models.Model):
    """Player relationship manager"""
    user = models.ForeignKey(
        User,
        related_name="players",
        on_delete=models.CASCADE,
    )
    club = models.ForeignKey(
        Club,
        related_name="club_players",
        on_delete=models.CASCADE,
    )
    player_info=models.OneToOneField(
        PlayerInfo,
        related_name="player",
        on_delete=models.CASCADE,
    )
    player_attr = models.OneToOneField(
        PlayerAttr,
        related_name="player_instance",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return object string."""
        return f"{self.user.username} // {self.player_info.name} ({self.club.club_info.name})"

    def goal_count(self):
        """Return ovr as percentage"""
        return self.goals.count()


class Fixture(models.Model):
    """Fixture model"""
    user = models.ForeignKey(
        User,
        related_name="fixtures",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    season = models.IntegerField(default=2020)
    matchday = models.IntegerField(default=1)
    home = models.ForeignKey(
        Club,
        related_name="home_fixtures",
        on_delete=models.CASCADE,
    )
    away = models.ForeignKey(
        Club,
        related_name="away_fixtures",
        on_delete=models.CASCADE,
    )
    played = models.BooleanField(
        default=False,
    )

    def __str__(self):
        """Return object string."""
        return f"Fixture: {self.home.club_info.name} v {self.away.club_info.name}"


class Goal(models.Model):
    """Goal model"""
    fixture = models.ForeignKey(
        Fixture,
        related_name="fixture_goals",
        on_delete=models.CASCADE,
    )
    minute = models.IntegerField()
    scorer = models.ForeignKey(
        Player,
        related_name="goals",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return object string."""
        return f"Goal: {self.scorer.player_info.name}"

class News(models.Model):
    """News model"""
    user = models.ForeignKey(
        User,
        related_name="news",
        on_delete=models.CASCADE,
    )
    player = models.ForeignKey(
        Player,
        related_name="player_news",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    club = models.ForeignKey(
        Club,
        related_name="club_news",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    message_id = models.IntegerField()
    sender = models.CharField(
        max_length=100,
    )
    subject = models.CharField(
        max_length=500,
    )
    body = models.TextField(
        default="""I am a wealthy Nigerian Prince and I need some help in moving my fortune to your
         country. I will reward you handsomely with many jewels and diamonds and monies. Please
         reply immediately with your bank details and personal information as so to proceed."""
    )
    offer = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True
    )
    read = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """Return object string."""
        return f"Subject: {self.subject}"
