from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MemberInfo, PlayingMember, HoleHandicap, Start1Hole1Player1, Start1Hole1Player2, PlayerCount, \
    Start1Hole1Player3, Start1Hole1Player4, Start1Hole1Player5, Start1Hole2Player1, Start1Hole2Player2, \
    Start1Hole2Player3, Start1Hole2Player4, Start1Hole2Player5, Start1Hole3Player1, Start1Hole3Player2, \
    Start1Hole3Player3, Start1Hole3Player4, Start1Hole3Player5, Start1Hole4Player1, Start1Hole4Player2, \
    Start1Hole4Player3, Start1Hole4Player4, Start1Hole4Player5, Start1Hole5Player1, Start1Hole5Player2, \
    Start1Hole5Player3, Start1Hole5Player4, Start1Hole5Player5, Start1Hole6Player1, Start1Hole6Player2, \
    Start1Hole6Player3, Start1Hole6Player4, Start1Hole6Player5, Start1Hole7Player1, Start1Hole7Player2, \
    Start1Hole7Player3, Start1Hole7Player4, Start1Hole7Player5, Start1Hole8Player1, Start1Hole8Player2, \
    Start1Hole8Player3, Start1Hole8Player4, Start1Hole8Player5, Start1Hole9Player1, Start1Hole9Player2, \
    Start1Hole9Player3, Start1Hole9Player4, Start1Hole9Player5, Start1Hole10Player1, Start1Hole10Player2, \
    Start1Hole10Player3, Start1Hole10Player4, Start1Hole10Player5, Start1Hole11Player1, Start1Hole11Player2, \
    Start1Hole11Player3, Start1Hole11Player4, Start1Hole11Player5, Start1Hole12Player1, Start1Hole12Player2, \
    Start1Hole12Player3, Start1Hole12Player4, Start1Hole12Player5, Start1Hole13Player1, Start1Hole13Player2, \
    Start1Hole13Player3, Start1Hole13Player4, Start1Hole13Player5, Start1Hole14Player1, Start1Hole14Player2, \
    Start1Hole14Player3, Start1Hole14Player4, Start1Hole14Player5, Start1Hole15Player1, Start1Hole15Player2, \
    Start1Hole15Player3, Start1Hole15Player4, Start1Hole15Player5, Start1Hole16Player1, Start1Hole16Player2, \
    Start1Hole16Player3, Start1Hole16Player4, Start1Hole16Player5, Start1Hole17Player1, Start1Hole17Player2, \
    Start1Hole17Player3, Start1Hole17Player4, Start1Hole17Player5, Start1Hole18Player1, Start1Hole18Player2, \
    Start1Hole18Player3, Start1Hole18Player4, Start1Hole18Player5, Skins, HoleAssignment, HoleAssignment2, \
    Start2Hole1Player1, Start2Hole1Player2, \
    Start2Hole1Player3, Start2Hole1Player4, Start2Hole1Player5, Start2Hole2Player1, Start2Hole2Player2, \
    Start2Hole2Player3, Start2Hole2Player4, Start2Hole2Player5, Start2Hole3Player1, Start2Hole3Player2, \
    Start2Hole3Player3, Start2Hole3Player4, Start2Hole3Player5, Start2Hole4Player1, Start2Hole4Player2, \
    Start2Hole4Player3, Start2Hole4Player4, Start2Hole4Player5, Start2Hole5Player1, Start2Hole5Player2, \
    Start2Hole5Player3, Start2Hole5Player4, Start2Hole5Player5, Start2Hole6Player1, Start2Hole6Player2, \
    Start2Hole6Player3, Start2Hole6Player4, Start2Hole6Player5, Start2Hole7Player1, Start2Hole7Player2, \
    Start2Hole7Player3, Start2Hole7Player4, Start2Hole7Player5, Start2Hole8Player1, Start2Hole8Player2, \
    Start2Hole8Player3, Start2Hole8Player4, Start2Hole8Player5, Start2Hole9Player1, Start2Hole9Player2, \
    Start2Hole9Player3, Start2Hole9Player4, Start2Hole9Player5, Start2Hole10Player1, Start2Hole10Player2, \
    Start2Hole10Player3, Start2Hole10Player4, Start2Hole10Player5, Start2Hole11Player1, Start2Hole11Player2, \
    Start2Hole11Player3, Start2Hole11Player4, Start2Hole11Player5, Start2Hole12Player1, Start2Hole12Player2, \
    Start2Hole12Player3, Start2Hole12Player4, Start2Hole12Player5, Start2Hole13Player1, Start2Hole13Player2, \
    Start2Hole13Player3, Start2Hole13Player4, Start2Hole13Player5, Start2Hole14Player1, Start2Hole14Player2, \
    Start2Hole14Player3, Start2Hole14Player4, Start2Hole14Player5, Start2Hole15Player1, Start2Hole15Player2, \
    Start2Hole15Player3, Start2Hole15Player4, Start2Hole15Player5, Start2Hole16Player1, Start2Hole16Player2, \
    Start2Hole16Player3, Start2Hole16Player4, Start2Hole16Player5, Start2Hole17Player1, Start2Hole17Player2, \
    Start2Hole17Player3, Start2Hole17Player4, Start2Hole17Player5, Start2Hole18Player1, Start2Hole18Player2, \
    Start2Hole18Player3, Start2Hole18Player4, Start2Hole18Player5, \
    Start3Hole1Player1, Start3Hole1Player2, \
    Start3Hole1Player3, Start3Hole1Player4, Start3Hole1Player5, Start3Hole2Player1, Start3Hole2Player2, \
    Start3Hole2Player3, Start3Hole2Player4, Start3Hole2Player5, Start3Hole3Player1, Start3Hole3Player2, \
    Start3Hole3Player3, Start3Hole3Player4, Start3Hole3Player5, Start3Hole4Player1, Start3Hole4Player2, \
    Start3Hole4Player3, Start3Hole4Player4, Start3Hole4Player5, Start3Hole5Player1, Start3Hole5Player2, \
    Start3Hole5Player3, Start3Hole5Player4, Start3Hole5Player5, Start3Hole6Player1, Start3Hole6Player2, \
    Start3Hole6Player3, Start3Hole6Player4, Start3Hole6Player5, Start3Hole7Player1, Start3Hole7Player2, \
    Start3Hole7Player3, Start3Hole7Player4, Start3Hole7Player5, Start3Hole8Player1, Start3Hole8Player2, \
    Start3Hole8Player3, Start3Hole8Player4, Start3Hole8Player5, Start3Hole9Player1, Start3Hole9Player2, \
    Start3Hole9Player3, Start3Hole9Player4, Start3Hole9Player5, Start3Hole10Player1, Start3Hole10Player2, \
    Start3Hole10Player3, Start3Hole10Player4, Start3Hole10Player5, Start3Hole11Player1, Start3Hole11Player2, \
    Start3Hole11Player3, Start3Hole11Player4, Start3Hole11Player5, Start3Hole12Player1, Start3Hole12Player2, \
    Start3Hole12Player3, Start3Hole12Player4, Start3Hole12Player5, Start3Hole13Player1, Start3Hole13Player2, \
    Start3Hole13Player3, Start3Hole13Player4, Start3Hole13Player5, Start3Hole14Player1, Start3Hole14Player2, \
    Start3Hole14Player3, Start3Hole14Player4, Start3Hole14Player5, Start3Hole15Player1, Start3Hole15Player2, \
    Start3Hole15Player3, Start3Hole15Player4, Start3Hole15Player5, Start3Hole16Player1, Start3Hole16Player2, \
    Start3Hole16Player3, Start3Hole16Player4, Start3Hole16Player5, Start3Hole17Player1, Start3Hole17Player2, \
    Start3Hole17Player3, Start3Hole17Player4, Start3Hole17Player5, Start3Hole18Player1, Start3Hole18Player2, \
    Start3Hole18Player3, Start3Hole18Player4, Start3Hole18Player5, \
    Start4Hole1Player1, Start4Hole1Player2, \
    Start4Hole1Player3, Start4Hole1Player4, Start4Hole1Player5, Start4Hole2Player1, Start4Hole2Player2, \
    Start4Hole2Player3, Start4Hole2Player4, Start4Hole2Player5, Start4Hole3Player1, Start4Hole3Player2, \
    Start4Hole3Player3, Start4Hole3Player4, Start4Hole3Player5, Start4Hole4Player1, Start4Hole4Player2, \
    Start4Hole4Player3, Start4Hole4Player4, Start4Hole4Player5, Start4Hole5Player1, Start4Hole5Player2, \
    Start4Hole5Player3, Start4Hole5Player4, Start4Hole5Player5, Start4Hole6Player1, Start4Hole6Player2, \
    Start4Hole6Player3, Start4Hole6Player4, Start4Hole6Player5, Start4Hole7Player1, Start4Hole7Player2, \
    Start4Hole7Player3, Start4Hole7Player4, Start4Hole7Player5, Start4Hole8Player1, Start4Hole8Player2, \
    Start4Hole8Player3, Start4Hole8Player4, Start4Hole8Player5, Start4Hole9Player1, Start4Hole9Player2, \
    Start4Hole9Player3, Start4Hole9Player4, Start4Hole9Player5, Start4Hole10Player1, Start4Hole10Player2, \
    Start4Hole10Player3, Start4Hole10Player4, Start4Hole10Player5, Start4Hole11Player1, Start4Hole11Player2, \
    Start4Hole11Player3, Start4Hole11Player4, Start4Hole11Player5, Start4Hole12Player1, Start4Hole12Player2, \
    Start4Hole12Player3, Start4Hole12Player4, Start4Hole12Player5, Start4Hole13Player1, Start4Hole13Player2, \
    Start4Hole13Player3, Start4Hole13Player4, Start4Hole13Player5, Start4Hole14Player1, Start4Hole14Player2, \
    Start4Hole14Player3, Start4Hole14Player4, Start4Hole14Player5, Start4Hole15Player1, Start4Hole15Player2, \
    Start4Hole15Player3, Start4Hole15Player4, Start4Hole15Player5, Start4Hole16Player1, Start4Hole16Player2, \
    Start4Hole16Player3, Start4Hole16Player4, Start4Hole16Player5, Start4Hole17Player1, Start4Hole17Player2, \
    Start4Hole17Player3, Start4Hole17Player4, Start4Hole17Player5, Start4Hole18Player1, Start4Hole18Player2, \
    Start4Hole18Player3, Start4Hole18Player4, Start4Hole18Player5, \
    Start5Hole1Player1, Start5Hole1Player2, \
    Start5Hole1Player3, Start5Hole1Player4, Start5Hole1Player5, Start5Hole2Player1, Start5Hole2Player2, \
    Start5Hole2Player3, Start5Hole2Player4, Start5Hole2Player5, Start5Hole3Player1, Start5Hole3Player2, \
    Start5Hole3Player3, Start5Hole3Player4, Start5Hole3Player5, Start5Hole4Player1, Start5Hole4Player2, \
    Start5Hole4Player3, Start5Hole4Player4, Start5Hole4Player5, Start5Hole5Player1, Start5Hole5Player2, \
    Start5Hole5Player3, Start5Hole5Player4, Start5Hole5Player5, Start5Hole6Player1, Start5Hole6Player2, \
    Start5Hole6Player3, Start5Hole6Player4, Start5Hole6Player5, Start5Hole7Player1, Start5Hole7Player2, \
    Start5Hole7Player3, Start5Hole7Player4, Start5Hole7Player5, Start5Hole8Player1, Start5Hole8Player2, \
    Start5Hole8Player3, Start5Hole8Player4, Start5Hole8Player5, Start5Hole9Player1, Start5Hole9Player2, \
    Start5Hole9Player3, Start5Hole9Player4, Start5Hole9Player5, Start5Hole10Player1, Start5Hole10Player2, \
    Start5Hole10Player3, Start5Hole10Player4, Start5Hole10Player5, Start5Hole11Player1, Start5Hole11Player2, \
    Start5Hole11Player3, Start5Hole11Player4, Start5Hole11Player5, Start5Hole12Player1, Start5Hole12Player2, \
    Start5Hole12Player3, Start5Hole12Player4, Start5Hole12Player5, Start5Hole13Player1, Start5Hole13Player2, \
    Start5Hole13Player3, Start5Hole13Player4, Start5Hole13Player5, Start5Hole14Player1, Start5Hole14Player2, \
    Start5Hole14Player3, Start5Hole14Player4, Start5Hole14Player5, Start5Hole15Player1, Start5Hole15Player2, \
    Start5Hole15Player3, Start5Hole15Player4, Start5Hole15Player5, Start5Hole16Player1, Start5Hole16Player2, \
    Start5Hole16Player3, Start5Hole16Player4, Start5Hole16Player5, Start5Hole17Player1, Start5Hole17Player2, \
    Start5Hole17Player3, Start5Hole17Player4, Start5Hole17Player5, Start5Hole18Player1, Start5Hole18Player2, \
    Start5Hole18Player3, Start5Hole18Player4, Start5Hole18Player5, \
    Start6Hole1Player1, Start6Hole1Player2, \
    Start6Hole1Player3, Start6Hole1Player4, Start6Hole1Player5, Start6Hole2Player1, Start6Hole2Player2, \
    Start6Hole2Player3, Start6Hole2Player4, Start6Hole2Player5, Start6Hole3Player1, Start6Hole3Player2, \
    Start6Hole3Player3, Start6Hole3Player4, Start6Hole3Player5, Start6Hole4Player1, Start6Hole4Player2, \
    Start6Hole4Player3, Start6Hole4Player4, Start6Hole4Player5, Start6Hole5Player1, Start6Hole5Player2, \
    Start6Hole5Player3, Start6Hole5Player4, Start6Hole5Player5, Start6Hole6Player1, Start6Hole6Player2, \
    Start6Hole6Player3, Start6Hole6Player4, Start6Hole6Player5, Start6Hole7Player1, Start6Hole7Player2, \
    Start6Hole7Player3, Start6Hole7Player4, Start6Hole7Player5, Start6Hole8Player1, Start6Hole8Player2, \
    Start6Hole8Player3, Start6Hole8Player4, Start6Hole8Player5, Start6Hole9Player1, Start6Hole9Player2, \
    Start6Hole9Player3, Start6Hole9Player4, Start6Hole9Player5, Start6Hole10Player1, Start6Hole10Player2, \
    Start6Hole10Player3, Start6Hole10Player4, Start6Hole10Player5, Start6Hole11Player1, Start6Hole11Player2, \
    Start6Hole11Player3, Start6Hole11Player4, Start6Hole11Player5, Start6Hole12Player1, Start6Hole12Player2, \
    Start6Hole12Player3, Start6Hole12Player4, Start6Hole12Player5, Start6Hole13Player1, Start6Hole13Player2, \
    Start6Hole13Player3, Start6Hole13Player4, Start6Hole13Player5, Start6Hole14Player1, Start6Hole14Player2, \
    Start6Hole14Player3, Start6Hole14Player4, Start6Hole14Player5, Start6Hole15Player1, Start6Hole15Player2, \
    Start6Hole15Player3, Start6Hole15Player4, Start6Hole15Player5, Start6Hole16Player1, Start6Hole16Player2, \
    Start6Hole16Player3, Start6Hole16Player4, Start6Hole16Player5, Start6Hole17Player1, Start6Hole17Player2, \
    Start6Hole17Player3, Start6Hole17Player4, Start6Hole17Player5, Start6Hole18Player1, Start6Hole18Player2, \
    Start6Hole18Player3, Start6Hole18Player4, Start6Hole18Player5, \
    Start7Hole1Player1, Start7Hole1Player2, \
    Start7Hole1Player3, Start7Hole1Player4, Start7Hole1Player5, Start7Hole2Player1, Start7Hole2Player2, \
    Start7Hole2Player3, Start7Hole2Player4, Start7Hole2Player5, Start7Hole3Player1, Start7Hole3Player2, \
    Start7Hole3Player3, Start7Hole3Player4, Start7Hole3Player5, Start7Hole4Player1, Start7Hole4Player2, \
    Start7Hole4Player3, Start7Hole4Player4, Start7Hole4Player5, Start7Hole5Player1, Start7Hole5Player2, \
    Start7Hole5Player3, Start7Hole5Player4, Start7Hole5Player5, Start7Hole6Player1, Start7Hole6Player2, \
    Start7Hole6Player3, Start7Hole6Player4, Start7Hole6Player5, Start7Hole7Player1, Start7Hole7Player2, \
    Start7Hole7Player3, Start7Hole7Player4, Start7Hole7Player5, Start7Hole8Player1, Start7Hole8Player2, \
    Start7Hole8Player3, Start7Hole8Player4, Start7Hole8Player5, Start7Hole9Player1, Start7Hole9Player2, \
    Start7Hole9Player3, Start7Hole9Player4, Start7Hole9Player5, Start7Hole10Player1, Start7Hole10Player2, \
    Start7Hole10Player3, Start7Hole10Player4, Start7Hole10Player5, Start7Hole11Player1, Start7Hole11Player2, \
    Start7Hole11Player3, Start7Hole11Player4, Start7Hole11Player5, Start7Hole12Player1, Start7Hole12Player2, \
    Start7Hole12Player3, Start7Hole12Player4, Start7Hole12Player5, Start7Hole13Player1, Start7Hole13Player2, \
    Start7Hole13Player3, Start7Hole13Player4, Start7Hole13Player5, Start7Hole14Player1, Start7Hole14Player2, \
    Start7Hole14Player3, Start7Hole14Player4, Start7Hole14Player5, Start7Hole15Player1, Start7Hole15Player2, \
    Start7Hole15Player3, Start7Hole15Player4, Start7Hole15Player5, Start7Hole16Player1, Start7Hole16Player2, \
    Start7Hole16Player3, Start7Hole16Player4, Start7Hole16Player5, Start7Hole17Player1, Start7Hole17Player2, \
    Start7Hole17Player3, Start7Hole17Player4, Start7Hole17Player5, Start7Hole18Player1, Start7Hole18Player2, \
    Start7Hole18Player3, Start7Hole18Player4, Start7Hole18Player5, \
    Start8Hole1Player1, Start8Hole1Player2, \
    Start8Hole1Player3, Start8Hole1Player4, Start8Hole1Player5, Start8Hole2Player1, Start8Hole2Player2, \
    Start8Hole2Player3, Start8Hole2Player4, Start8Hole2Player5, Start8Hole3Player1, Start8Hole3Player2, \
    Start8Hole3Player3, Start8Hole3Player4, Start8Hole3Player5, Start8Hole4Player1, Start8Hole4Player2, \
    Start8Hole4Player3, Start8Hole4Player4, Start8Hole4Player5, Start8Hole5Player1, Start8Hole5Player2, \
    Start8Hole5Player3, Start8Hole5Player4, Start8Hole5Player5, Start8Hole6Player1, Start8Hole6Player2, \
    Start8Hole6Player3, Start8Hole6Player4, Start8Hole6Player5, Start8Hole7Player1, Start8Hole7Player2, \
    Start8Hole7Player3, Start8Hole7Player4, Start8Hole7Player5, Start8Hole8Player1, Start8Hole8Player2, \
    Start8Hole8Player3, Start8Hole8Player4, Start8Hole8Player5, Start8Hole9Player1, Start8Hole9Player2, \
    Start8Hole9Player3, Start8Hole9Player4, Start8Hole9Player5, Start8Hole10Player1, Start8Hole10Player2, \
    Start8Hole10Player3, Start8Hole10Player4, Start8Hole10Player5, Start8Hole11Player1, Start8Hole11Player2, \
    Start8Hole11Player3, Start8Hole11Player4, Start8Hole11Player5, Start8Hole12Player1, Start8Hole12Player2, \
    Start8Hole12Player3, Start8Hole12Player4, Start8Hole12Player5, Start8Hole13Player1, Start8Hole13Player2, \
    Start8Hole13Player3, Start8Hole13Player4, Start8Hole13Player5, Start8Hole14Player1, Start8Hole14Player2, \
    Start8Hole14Player3, Start8Hole14Player4, Start8Hole14Player5, Start8Hole15Player1, Start8Hole15Player2, \
    Start8Hole15Player3, Start8Hole15Player4, Start8Hole15Player5, Start8Hole16Player1, Start8Hole16Player2, \
    Start8Hole16Player3, Start8Hole16Player4, Start8Hole16Player5, Start8Hole17Player1, Start8Hole17Player2, \
    Start8Hole17Player3, Start8Hole17Player4, Start8Hole17Player5, Start8Hole18Player1, Start8Hole18Player2, \
    Start8Hole18Player3, Start8Hole18Player4, Start8Hole18Player5, \
    Start9Hole1Player1, Start9Hole1Player2, \
    Start9Hole1Player3, Start9Hole1Player4, Start9Hole1Player5, Start9Hole2Player1, Start9Hole2Player2, \
    Start9Hole2Player3, Start9Hole2Player4, Start9Hole2Player5, Start9Hole3Player1, Start9Hole3Player2, \
    Start9Hole3Player3, Start9Hole3Player4, Start9Hole3Player5, Start9Hole4Player1, Start9Hole4Player2, \
    Start9Hole4Player3, Start9Hole4Player4, Start9Hole4Player5, Start9Hole5Player1, Start9Hole5Player2, \
    Start9Hole5Player3, Start9Hole5Player4, Start9Hole5Player5, Start9Hole6Player1, Start9Hole6Player2, \
    Start9Hole6Player3, Start9Hole6Player4, Start9Hole6Player5, Start9Hole7Player1, Start9Hole7Player2, \
    Start9Hole7Player3, Start9Hole7Player4, Start9Hole7Player5, Start9Hole8Player1, Start9Hole8Player2, \
    Start9Hole8Player3, Start9Hole8Player4, Start9Hole8Player5, Start9Hole9Player1, Start9Hole9Player2, \
    Start9Hole9Player3, Start9Hole9Player4, Start9Hole9Player5, Start9Hole10Player1, Start9Hole10Player2, \
    Start9Hole10Player3, Start9Hole10Player4, Start9Hole10Player5, Start9Hole11Player1, Start9Hole11Player2, \
    Start9Hole11Player3, Start9Hole11Player4, Start9Hole11Player5, Start9Hole12Player1, Start9Hole12Player2, \
    Start9Hole12Player3, Start9Hole12Player4, Start9Hole12Player5, Start9Hole13Player1, Start9Hole13Player2, \
    Start9Hole13Player3, Start9Hole13Player4, Start9Hole13Player5, Start9Hole14Player1, Start9Hole14Player2, \
    Start9Hole14Player3, Start9Hole14Player4, Start9Hole14Player5, Start9Hole15Player1, Start9Hole15Player2, \
    Start9Hole15Player3, Start9Hole15Player4, Start9Hole15Player5, Start9Hole16Player1, Start9Hole16Player2, \
    Start9Hole16Player3, Start9Hole16Player4, Start9Hole16Player5, Start9Hole17Player1, Start9Hole17Player2, \
    Start9Hole17Player3, Start9Hole17Player4, Start9Hole17Player5, Start9Hole18Player1, Start9Hole18Player2, \
    Start9Hole18Player3, Start9Hole18Player4, Start9Hole18Player5



class CountPlayers(forms.ModelForm):

    class Meta:
        model = PlayerCount
        fields = [
            'count',


        ]



class SkinsForm(forms.ModelForm):

    class Meta:
        model = Skins
        fields = [
            'memberid',
            'firstname',
            'lastname',
            'skinhole',
            'score',

        ]




class GolferInfo(forms.ModelForm):

    class Meta:
        model = MemberInfo
        fields = [
            'memberid',
            'firstname',
            'lastname',
            'add1',
            'add2',
            'city',
            'st',
            'zipcode',
            'cell',
            'home',
            'email',
            'handicap',
            'chgopt9',
            'chpt18',
            'handicap18',
            'playing',
        ]


class HandicapHoles(forms.ModelForm):

    class Meta:
        model = HoleHandicap
        fields = [
            'hole1handicap',
            'hole2handicap',
            'hole3handicap',
            'hole4handicap',
            'hole5handicap',
            'hole6handicap',
            'hole7handicap',
            'hole8handicap',
            'hole9handicap',
            'hole10handicap',
            'hole11handicap',
            'hole12handicap',
            'hole13handicap',
            'hole14handicap',
            'hole15handicap',
            'hole16handicap',
            'hole17handicap',
            'hole18handicap',
        ]


class PlayingMembers(forms.ModelForm):

    class Meta:
        model = PlayingMember
        fields = [
            'memberid',
            'firstname',
            'lastname',
            'handicap',
            'starthole',
        ]


class PLayer1Hole1Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole1Player1
        fields = [
            'memberid',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole1Player2
        fields = [
            'memberid2',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole1Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole1Player3
        fields = [
            'memberid3',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole1Player4
        fields = [
            'memberid4',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole1Player5
        fields = [
            'memberid5',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole2Player1
        fields = [
            'memberid21',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole2Player2
        fields = [
            'memberid22',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole2Player3
        fields = [
            'memberid23',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole2Player4
        fields = [
            'memberid24',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole2Player5
        fields = [
            'memberid25',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole3Player1
        fields = [
            'memberid31',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole3Player2
        fields = [
            'memberid32',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole3Player3
        fields = [
            'memberid33',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole3Player4
        fields = [
            'memberid34',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole3Player5
        fields = [
            'memberid35',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole4Player1
        fields = [
            'memberid41',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole4Player2
        fields = [
            'memberid42',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole4Player3
        fields = [
            'memberid43',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole4Player4
        fields = [
            'memberid44',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole4Player5
        fields = [
            'memberid45',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole5Player1
        fields = [
            'memberid51',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole5Player2
        fields = [
            'memberid52',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole5Player3
        fields = [
            'memberid53',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole5Player4
        fields = [
            'memberid54',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole5Player5
        fields = [
            'memberid55',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole6Player1
        fields = [
            'memberid61',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole6Player2
        fields = [
            'memberid62',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole6Player3
        fields = [
            'memberid63',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole6Player4
        fields = [
            'memberid64',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole6Player5
        fields = [
            'memberid65',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole7Player1
        fields = [
            'memberid71',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole7Player2
        fields = [
            'memberid72',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole7Player3
        fields = [
            'memberid73',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole7Player4
        fields = [
            'memberid74',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole7Player5
        fields = [
            'memberid75',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole8Player1
        fields = [
            'memberid81',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole8Player2
        fields = [
            'memberid82',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole8Player3
        fields = [
            'memberid83',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole8Player4
        fields = [
            'memberid84',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole8Player5
        fields = [
            'memberid85',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole9Player1
        fields = [
            'memberid91',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole9Player2
        fields = [
            'memberid92',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole9Player3
        fields = [
            'memberid93',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole9Player4
        fields = [
            'memberid94',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole9Player5
        fields = [
            'memberid95',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole10Player1
        fields = [
            'memberid101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole10Player2
        fields = [
            'memberid102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole10Player3
        fields = [
            'memberid103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole10Player4
        fields = [
            'memberid104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole10Player5
        fields = [
            'memberid105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole11Player1
        fields = [
            'memberid111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole11Player2
        fields = [
            'memberid112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole11Player3
        fields = [
            'memberid113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole11Player4
        fields = [
            'memberid114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole11Player5
        fields = [
            'memberid115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole12Player1
        fields = [
            'memberid121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole12Player2
        fields = [
            'memberid122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole12Player3
        fields = [
            'memberid123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole12Player4
        fields = [
            'memberid124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole12Player5
        fields = [
            'memberid125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole13Player1
        fields = [
            'memberid131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole13Player2
        fields = [
            'memberid132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole13Player3
        fields = [
            'memberid133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole13Player4
        fields = [
            'memberid134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole13Player5
        fields = [
            'memberid135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole14Player1
        fields = [
            'memberid141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole14Player2
        fields = [
            'memberid142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole14Player3
        fields = [
            'memberid143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole14Player4
        fields = [
            'memberid144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole14Player5
        fields = [
            'memberid145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole15Player1
        fields = [
            'memberid151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole15Player2
        fields = [
            'memberid152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole15Player3
        fields = [
            'memberid153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole15Player4
        fields = [
            'memberid154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole15Player5
        fields = [
            'memberid155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole16Player1
        fields = [
            'memberid161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole16Player2
        fields = [
            'memberid162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole16Player3
        fields = [
            'memberid163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole16Player4
        fields = [
            'memberid164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole16Player5
        fields = [
            'memberid165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole17Player1
        fields = [
            'memberid171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole17Player2
        fields = [
            'memberid172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole17Player3
        fields = [
            'memberid173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole17Player4
        fields = [
            'memberid174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole17Player5
        fields = [
            'memberid175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole18Player1
        fields = [
            'memberid181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole18Player2
        fields = [
            'memberid182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole18Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole18Player3
        fields = [
            'memberid183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole18Player4
        fields = [
            'memberid184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start1(forms.ModelForm):

    class Meta:
        model = Start1Hole18Player5
        fields = [
            'memberid185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole1Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole1Player1
        fields = [
            'memberid211',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole1Player2
        fields = [
            'memberid212',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole1Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole1Player3
        fields = [
            'memberid213',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole1Player4
        fields = [
            'memberid214',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole1Player5
        fields = [
            'memberid215',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole2Player1
        fields = [
            'memberid221',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole2Player2
        fields = [
            'memberid222',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole2Player3
        fields = [
            'memberid223',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole2Player4
        fields = [
            'memberid224',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole2Player5
        fields = [
            'memberid225',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole3Player1
        fields = [
            'memberid231',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole3Player2
        fields = [
            'memberid232',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole3Player3
        fields = [
            'memberid233',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole3Player4
        fields = [
            'memberid234',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole3Player5
        fields = [
            'memberid235',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole4Player1
        fields = [
            'memberid241',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole4Player2
        fields = [
            'memberid242',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole4Player3
        fields = [
            'memberid243',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole4Player4
        fields = [
            'memberid244',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole4Player5
        fields = [
            'memberid245',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole5Player1
        fields = [
            'memberid251',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole5Player2
        fields = [
            'memberid252',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole5Player3
        fields = [
            'memberid253',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole5Player4
        fields = [
            'memberid254',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole5Player5
        fields = [
            'memberid255',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole6Player1
        fields = [
            'memberid261',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole6Player2
        fields = [
            'memberid262',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole6Player3
        fields = [
            'memberid263',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole6Player4
        fields = [
            'memberid264',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole6Player5
        fields = [
            'memberid265',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole7Player1
        fields = [
            'memberid271',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole7Player2
        fields = [
            'memberid272',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole7Player3
        fields = [
            'memberid273',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole7Player4
        fields = [
            'memberid274',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole7Player5
        fields = [
            'memberid275',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole8Player1
        fields = [
            'memberid281',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole8Player2
        fields = [
            'memberid282',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole8Player3
        fields = [
            'memberid283',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole8Player4
        fields = [
            'memberid284',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole8Player5
        fields = [
            'memberid285',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole9Player1
        fields = [
            'memberid291',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole9Player2
        fields = [
            'memberid292',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole9Player3
        fields = [
            'memberid293',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole9Player4
        fields = [
            'memberid294',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole9Player5
        fields = [
            'memberid295',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole10Player1
        fields = [
            'memberid2101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole10Player2
        fields = [
            'memberid2102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole10Player3
        fields = [
            'memberid2103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole10Player4
        fields = [
            'memberid2104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole10Player5
        fields = [
            'memberid2105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole11Player1
        fields = [
            'memberid2111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole11Player2
        fields = [
            'memberid2112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole11Player3
        fields = [
            'memberid2113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole11Player4
        fields = [
            'memberid2114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole11Player5
        fields = [
            'memberid2115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole12Player1
        fields = [
            'memberid2121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole12Player2
        fields = [
            'memberid2122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole12Player3
        fields = [
            'memberid2123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole12Player4
        fields = [
            'memberid2124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole12Player5
        fields = [
            'memberid2125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole13Player1
        fields = [
            'memberid2131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole13Player2
        fields = [
            'memberid2132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole13Player3
        fields = [
            'memberid2133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole13Player4
        fields = [
            'memberid2134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole13Player5
        fields = [
            'memberid2135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole14Player1
        fields = [
            'memberid2141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole14Player2
        fields = [
            'memberid2142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole14Player3
        fields = [
            'memberid2143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole14Player4
        fields = [
            'memberid2144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole14Player5
        fields = [
            'memberid2145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole15Player1
        fields = [
            'memberid2151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole15Player2
        fields = [
            'memberid2152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole15Player3
        fields = [
            'memberid2153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole15Player4
        fields = [
            'memberid2154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole15Player5
        fields = [
            'memberid2155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole16Player1
        fields = [
            'memberid2161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole16Player2
        fields = [
            'memberid2162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole16Player3
        fields = [
            'memberid2163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole16Player4
        fields = [
            'memberid2164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole16Player5
        fields = [
            'memberid2165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole17Player1
        fields = [
            'memberid2171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole17Player2
        fields = [
            'memberid2172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole17Player3
        fields = [
            'memberid2173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole17Player4
        fields = [
            'memberid2174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole17Player5
        fields = [
            'memberid2175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole18Player1
        fields = [
            'memberid2181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole18Player2
        fields = [
            'memberid2182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',

            'score2',
    ]


class PLayer3Hole18Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole18Player3
        fields = [
            'memberid2183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole18Player4
        fields = [
            'memberid2184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start2(forms.ModelForm):

    class Meta:
        model = Start2Hole18Player5
        fields = [
            'memberid2185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player1
        fields = [
            'memberid311',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player2
        fields = [
            'memberid312',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]

############## Start 3 ###############

class PLayer1Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player1
        fields = [
            'memberid311',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player2
        fields = [
            'memberid312',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]



class PLayer3Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player3
        fields = [
            'memberid313',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player4
        fields = [
            'memberid314',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole1Player5
        fields = [
            'memberid315',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole2Player1
        fields = [
            'memberid321',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole2Player2
        fields = [
            'memberid322',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole2Player3
        fields = [
            'memberid323',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole2Player4
        fields = [
            'memberid324',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole2Player5
        fields = [
            'memberid325',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole3Player1
        fields = [
            'memberid331',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole3Player2
        fields = [
            'memberid332',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole3Player3
        fields = [
            'memberid333',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole3Player4
        fields = [
            'memberid334',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole3Player5
        fields = [
            'memberid335',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole4Player1
        fields = [
            'memberid341',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole4Player2
        fields = [
            'memberid342',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole4Player3
        fields = [
            'memberid343',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole4Player4
        fields = [
            'memberid344',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole4Player5
        fields = [
            'memberid345',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole5Player1
        fields = [
            'memberid351',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole5Player2
        fields = [
            'memberid352',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole5Player3
        fields = [
            'memberid353',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole5Player4
        fields = [
            'memberid354',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole5Player5
        fields = [
            'memberid355',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole6Player1
        fields = [
            'memberid361',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole6Player2
        fields = [
            'memberid362',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole6Player3
        fields = [
            'memberid363',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole6Player4
        fields = [
            'memberid364',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole6Player5
        fields = [
            'memberid365',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole7Player1
        fields = [
            'memberid371',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole7Player2
        fields = [
            'memberid372',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole7Player3
        fields = [
            'memberid373',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole7Player4
        fields = [
            'memberid374',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole7Player5
        fields = [
            'memberid375',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole8Player1
        fields = [
            'memberid381',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole8Player2
        fields = [
            'memberid382',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole8Player3
        fields = [
            'memberid383',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole8Player4
        fields = [
            'memberid384',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole8Player5
        fields = [
            'memberid385',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole9Player1
        fields = [
            'memberid391',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole9Player2
        fields = [
            'memberid392',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole9Player3
        fields = [
            'memberid393',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole9Player4
        fields = [
            'memberid394',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole9Player5
        fields = [
            'memberid395',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole10Player1
        fields = [
            'memberid3101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole10Player2
        fields = [
            'memberid3102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole10Player3
        fields = [
            'memberid3103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole10Player4
        fields = [
            'memberid3104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole10Player5
        fields = [
            'memberid3105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole11Player1
        fields = [
            'memberid3111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole11Player2
        fields = [
            'memberid3112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole11Player3
        fields = [
            'memberid3113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole11Player4
        fields = [
            'memberid3114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole11Player5
        fields = [
            'memberid3115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole12Player1
        fields = [
            'memberid3121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole12Player2
        fields = [
            'memberid3122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole12Player3
        fields = [
            'memberid3123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole12Player4
        fields = [
            'memberid3124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole12Player5
        fields = [
            'memberid3125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole13Player1
        fields = [
            'memberid3131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole13Player2
        fields = [
            'memberid3132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole13Player3
        fields = [
            'memberid3133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole13Player4
        fields = [
            'memberid3134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole13Player5
        fields = [
            'memberid3135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole14Player1
        fields = [
            'memberid3141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole14Player2
        fields = [
            'memberid3142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole14Player3
        fields = [
            'memberid3143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole14Player4
        fields = [
            'memberid3144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole14Player5
        fields = [
            'memberid3145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole15Player1
        fields = [
            'memberid3151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole15Player2
        fields = [
            'memberid3152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole15Player3
        fields = [
            'memberid3153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole15Player4
        fields = [
            'memberid3154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole15Player5
        fields = [
            'memberid3155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole16Player1
        fields = [
            'memberid3161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole16Player2
        fields = [
            'memberid3162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole16Player3
        fields = [
            'memberid3163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole16Player4
        fields = [
            'memberid3164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole16Player5
        fields = [
            'memberid3165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole17Player1
        fields = [
            'memberid3171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole17Player2
        fields = [
            'memberid3172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole17Player3
        fields = [
            'memberid3173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole17Player4
        fields = [
            'memberid3174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole17Player5
        fields = [
            'memberid3175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole18Player1
        fields = [
            'memberid3181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole18Player2
        fields = [
            'memberid3182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',

            'score2',
    ]


class PLayer3Hole18Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole18Player3
        fields = [
            'memberid3183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole18Player4
        fields = [
            'memberid3184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start3(forms.ModelForm):

    class Meta:
        model = Start3Hole18Player5
        fields = [
            'memberid3185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]
    
        
############## Start 4 ###############


class PLayer1Hole1Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole1Player1
        fields = [
            'memberid411',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole1Player2
        fields = [
            'memberid412',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]

class PLayer3Hole1Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole1Player3
        fields = [
            'memberid413',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole1Player4
        fields = [
            'memberid414',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole1Player5
        fields = [
            'memberid415',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole2Player1
        fields = [
            'memberid421',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole2Player2
        fields = [
            'memberid422',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole2Player3
        fields = [
            'memberid423',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole2Player4
        fields = [
            'memberid424',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole2Player5
        fields = [
            'memberid425',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole3Player1
        fields = [
            'memberid431',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole3Player2
        fields = [
            'memberid432',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole3Player3
        fields = [
            'memberid433',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole3Player4
        fields = [
            'memberid434',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole3Player5
        fields = [
            'memberid435',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole4Player1
        fields = [
            'memberid441',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole4Player2
        fields = [
            'memberid442',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole4Player3
        fields = [
            'memberid443',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole4Player4
        fields = [
            'memberid444',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole4Player5
        fields = [
            'memberid445',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole5Player1
        fields = [
            'memberid451',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole5Player2
        fields = [
            'memberid452',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole5Player3
        fields = [
            'memberid453',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole5Player4
        fields = [
            'memberid454',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole5Player5
        fields = [
            'memberid455',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole6Player1
        fields = [
            'memberid461',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole6Player2
        fields = [
            'memberid462',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole6Player3
        fields = [
            'memberid463',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole6Player4
        fields = [
            'memberid464',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole6Player5
        fields = [
            'memberid465',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole7Player1
        fields = [
            'memberid471',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole7Player2
        fields = [
            'memberid472',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole7Player3
        fields = [
            'memberid473',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole7Player4
        fields = [
            'memberid474',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole7Player5
        fields = [
            'memberid475',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole8Player1
        fields = [
            'memberid481',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole8Player2
        fields = [
            'memberid482',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole8Player3
        fields = [
            'memberid483',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole8Player4
        fields = [
            'memberid484',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole8Player5
        fields = [
            'memberid485',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole9Player1
        fields = [
            'memberid491',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole9Player2
        fields = [
            'memberid492',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole9Player3
        fields = [
            'memberid493',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole9Player4
        fields = [
            'memberid494',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole9Player5
        fields = [
            'memberid495',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole10Player1
        fields = [
            'memberid4101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole10Player2
        fields = [
            'memberid4102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole10Player3
        fields = [
            'memberid4103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole10Player4
        fields = [
            'memberid4104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole10Player5
        fields = [
            'memberid4105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole11Player1
        fields = [
            'memberid4111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole11Player2
        fields = [
            'memberid4112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole11Player3
        fields = [
            'memberid4113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole11Player4
        fields = [
            'memberid4114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole11Player5
        fields = [
            'memberid4115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole12Player1
        fields = [
            'memberid4121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole12Player2
        fields = [
            'memberid4122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole12Player3
        fields = [
            'memberid4123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole12Player4
        fields = [
            'memberid4124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole12Player5
        fields = [
            'memberid4125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole13Player1
        fields = [
            'memberid4131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole13Player2
        fields = [
            'memberid4132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole13Player3
        fields = [
            'memberid4133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole13Player4
        fields = [
            'memberid4134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole13Player5
        fields = [
            'memberid4135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole14Player1
        fields = [
            'memberid4141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole14Player2
        fields = [
            'memberid4142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole14Player3
        fields = [
            'memberid4143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole14Player4
        fields = [
            'memberid4144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole14Player5
        fields = [
            'memberid4145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole15Player1
        fields = [
            'memberid4151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole15Player2
        fields = [
            'memberid4152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole15Player3
        fields = [
            'memberid4153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole15Player4
        fields = [
            'memberid4154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole15Player5
        fields = [
            'memberid4155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole16Player1
        fields = [
            'memberid4161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole16Player2
        fields = [
            'memberid4162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole16Player3
        fields = [
            'memberid4163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole16Player4
        fields = [
            'memberid4164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole16Player5
        fields = [
            'memberid4165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole17Player1
        fields = [
            'memberid4171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole17Player2
        fields = [
            'memberid4172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole17Player3
        fields = [
            'memberid4173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole17Player4
        fields = [
            'memberid4174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole17Player5
        fields = [
            'memberid4175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole18Player1
        fields = [
            'memberid4181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole18Player2
        fields = [
            'memberid4182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',

            'score2',
    ]


class PLayer3Hole18Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole18Player3
        fields = [
            'memberid4183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole18Player4
        fields = [
            'memberid4184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start4(forms.ModelForm):

    class Meta:
        model = Start4Hole18Player5
        fields = [
            'memberid4185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]
        
        
############## Start 5 ###############


class PLayer1Hole1Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole1Player1
        fields = [
            'memberid511',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole1Player2
        fields = [
            'memberid512',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]

class PLayer3Hole1Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole1Player3
        fields = [
            'memberid513',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole1Player4
        fields = [
            'memberid514',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole1Player5
        fields = [
            'memberid515',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole2Player1
        fields = [
            'memberid521',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole2Player2
        fields = [
            'memberid522',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole2Player3
        fields = [
            'memberid523',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole2Player4
        fields = [
            'memberid524',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole2Player5
        fields = [
            'memberid525',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole3Player1
        fields = [
            'memberid531',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole3Player2
        fields = [
            'memberid532',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole3Player3
        fields = [
            'memberid533',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole3Player4
        fields = [
            'memberid534',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole3Player5
        fields = [
            'memberid535',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole4Player1
        fields = [
            'memberid541',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole4Player2
        fields = [
            'memberid542',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole4Player3
        fields = [
            'memberid543',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole4Player4
        fields = [
            'memberid544',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole4Player5
        fields = [
            'memberid545',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole5Player1
        fields = [
            'memberid551',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole5Player2
        fields = [
            'memberid552',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole5Player3
        fields = [
            'memberid553',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole5Player4
        fields = [
            'memberid554',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole5Player5
        fields = [
            'memberid555',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole6Player1
        fields = [
            'memberid561',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole6Player2
        fields = [
            'memberid562',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole6Player3
        fields = [
            'memberid563',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole6Player4
        fields = [
            'memberid564',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole6Player5
        fields = [
            'memberid565',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole7Player1
        fields = [
            'memberid571',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole7Player2
        fields = [
            'memberid572',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole7Player3
        fields = [
            'memberid573',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole7Player4
        fields = [
            'memberid574',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole7Player5
        fields = [
            'memberid575',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole8Player1
        fields = [
            'memberid581',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole8Player2
        fields = [
            'memberid582',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole8Player3
        fields = [
            'memberid583',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole8Player4
        fields = [
            'memberid584',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole8Player5
        fields = [
            'memberid585',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole9Player1
        fields = [
            'memberid591',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole9Player2
        fields = [
            'memberid592',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole9Player3
        fields = [
            'memberid593',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole9Player4
        fields = [
            'memberid594',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole9Player5
        fields = [
            'memberid595',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole10Player1
        fields = [
            'memberid5101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole10Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole10Player2
        fields = [
            'memberid5102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole10Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole10Player3
        fields = [
            'memberid5103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole10Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole10Player4
        fields = [
            'memberid5104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole10Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole10Player5
        fields = [
            'memberid5105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole11Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole11Player1
        fields = [
            'memberid5111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole11Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole11Player2
        fields = [
            'memberid5112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole11Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole11Player3
        fields = [
            'memberid5113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole11Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole11Player4
        fields = [
            'memberid5114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole11Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole11Player5
        fields = [
            'memberid5115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole12Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole12Player1
        fields = [
            'memberid5121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole12Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole12Player2
        fields = [
            'memberid5122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole12Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole12Player3
        fields = [
            'memberid5123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole12Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole12Player4
        fields = [
            'memberid5124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole12Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole12Player5
        fields = [
            'memberid5125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole13Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole13Player1
        fields = [
            'memberid5131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole13Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole13Player2
        fields = [
            'memberid5132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole13Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole13Player3
        fields = [
            'memberid5133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole13Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole13Player4
        fields = [
            'memberid5134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole13Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole13Player5
        fields = [
            'memberid5135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole14Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole14Player1
        fields = [
            'memberid5141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole14Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole14Player2
        fields = [
            'memberid5142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole14Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole14Player3
        fields = [
            'memberid5143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole14Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole14Player4
        fields = [
            'memberid5144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole14Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole14Player5
        fields = [
            'memberid5145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole15Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole15Player1
        fields = [
            'memberid5151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole15Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole15Player2
        fields = [
            'memberid5152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole15Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole15Player3
        fields = [
            'memberid5153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole15Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole15Player4
        fields = [
            'memberid5154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole15Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole15Player5
        fields = [
            'memberid5155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole16Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole16Player1
        fields = [
            'memberid5161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole16Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole16Player2
        fields = [
            'memberid5162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole16Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole16Player3
        fields = [
            'memberid5163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole16Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole16Player4
        fields = [
            'memberid5164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole16Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole16Player5
        fields = [
            'memberid5165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole17Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole17Player1
        fields = [
            'memberid5171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole17Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole17Player2
        fields = [
            'memberid5172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole17Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole17Player3
        fields = [
            'memberid5173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole17Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole17Player4
        fields = [
            'memberid5174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole17Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole17Player5
        fields = [
            'memberid5175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole18Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole18Player1
        fields = [
            'memberid5181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole18Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole18Player2
        fields = [
            'memberid5182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole18Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole18Player3
        fields = [
            'memberid5183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole18Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole18Player4
        fields = [
            'memberid5184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole18Start5(forms.ModelForm):

    class Meta:
        model = Start5Hole18Player5
        fields = [
            'memberid5185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]
        
        
############## Start 6 ###############


class PLayer1Hole1Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole1Player1
        fields = [
            'memberid611',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole1Player2
        fields = [
            'memberid612',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]

class PLayer3Hole1Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole1Player3
        fields = [
            'memberid613',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole1Player4
        fields = [
            'memberid614',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole1Player5
        fields = [
            'memberid615',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole2Player1
        fields = [
            'memberid621',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole2Player2
        fields = [
            'memberid622',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole2Player3
        fields = [
            'memberid623',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole2Player4
        fields = [
            'memberid624',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole2Player5
        fields = [
            'memberid625',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole3Player1
        fields = [
            'memberid631',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole3Player2
        fields = [
            'memberid632',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole3Player3
        fields = [
            'memberid633',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole3Player4
        fields = [
            'memberid634',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole3Player5
        fields = [
            'memberid635',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole4Player1
        fields = [
            'memberid641',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole4Player2
        fields = [
            'memberid642',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole4Player3
        fields = [
            'memberid643',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole4Player4
        fields = [
            'memberid644',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole4Player5
        fields = [
            'memberid645',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole5Player1
        fields = [
            'memberid651',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole5Player2
        fields = [
            'memberid652',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole5Player3
        fields = [
            'memberid653',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole5Player4
        fields = [
            'memberid654',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole5Player5
        fields = [
            'memberid655',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole6Player1
        fields = [
            'memberid661',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole6Player2
        fields = [
            'memberid662',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole6Player3
        fields = [
            'memberid663',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole6Player4
        fields = [
            'memberid664',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole6Player5
        fields = [
            'memberid665',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole7Player1
        fields = [
            'memberid671',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole7Player2
        fields = [
            'memberid672',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole7Player3
        fields = [
            'memberid673',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole7Player4
        fields = [
            'memberid674',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole7Player5
        fields = [
            'memberid675',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole8Player1
        fields = [
            'memberid681',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole8Player2
        fields = [
            'memberid682',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole8Player3
        fields = [
            'memberid683',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole8Player4
        fields = [
            'memberid684',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole8Player5
        fields = [
            'memberid685',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole9Player1
        fields = [
            'memberid691',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole9Player2
        fields = [
            'memberid692',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole9Player3
        fields = [
            'memberid693',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole9Player4
        fields = [
            'memberid694',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole9Player5
        fields = [
            'memberid695',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole10Player1
        fields = [
            'memberid6101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole10Player2
        fields = [
            'memberid6102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole10Player3
        fields = [
            'memberid6103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole10Player4
        fields = [
            'memberid6104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole10Player5
        fields = [
            'memberid6105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole11Player1
        fields = [
            'memberid6111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole11Player2
        fields = [
            'memberid6112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole11Player3
        fields = [
            'memberid6113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole11Player4
        fields = [
            'memberid6114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole11Player5
        fields = [
            'memberid6115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole12Player1
        fields = [
            'memberid6121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole12Player2
        fields = [
            'memberid6122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole12Player3
        fields = [
            'memberid6123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole12Player4
        fields = [
            'memberid6124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole12Player5
        fields = [
            'memberid6125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole13Player1
        fields = [
            'memberid6131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole13Player2
        fields = [
            'memberid6132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole13Player3
        fields = [
            'memberid6133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole13Player4
        fields = [
            'memberid6134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole13Player5
        fields = [
            'memberid6135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole14Player1
        fields = [
            'memberid6141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole14Player2
        fields = [
            'memberid6142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole14Player3
        fields = [
            'memberid6143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole14Player4
        fields = [
            'memberid6144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole14Player5
        fields = [
            'memberid6145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole15Player1
        fields = [
            'memberid6151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole15Player2
        fields = [
            'memberid6152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole15Player3
        fields = [
            'memberid6153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole15Player4
        fields = [
            'memberid6154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole15Player5
        fields = [
            'memberid6155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole16Player1
        fields = [
            'memberid6161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole16Player2
        fields = [
            'memberid6162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole16Player3
        fields = [
            'memberid6163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole16Player4
        fields = [
            'memberid6164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole16Player5
        fields = [
            'memberid6165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole17Player1
        fields = [
            'memberid6171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole17Player2
        fields = [
            'memberid6172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole17Player3
        fields = [
            'memberid6173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole17Player4
        fields = [
            'memberid6174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole17Player5
        fields = [
            'memberid6175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole18Player1
        fields = [
            'memberid6181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole18Player2
        fields = [
            'memberid6182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',

            'score2',
    ]


class PLayer3Hole18Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole18Player3
        fields = [
            'memberid6183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole18Player4
        fields = [
            'memberid6184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start6(forms.ModelForm):

    class Meta:
        model = Start6Hole18Player5
        fields = [
            'memberid6185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]
        
############## Start 7 ###############


class PLayer1Hole1Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole1Player1
        fields = [
            'memberid711',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole1Player2
        fields = [
            'memberid712',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]

class PLayer3Hole1Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole1Player3
        fields = [
            'memberid713',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole1Player4
        fields = [
            'memberid714',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole1Player5
        fields = [
            'memberid715',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole2Player1
        fields = [
            'memberid721',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole2Player2
        fields = [
            'memberid722',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole2Player3
        fields = [
            'memberid723',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole2Player4
        fields = [
            'memberid724',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole2Player5
        fields = [
            'memberid725',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole3Player1
        fields = [
            'memberid731',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole3Player2
        fields = [
            'memberid732',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole3Player3
        fields = [
            'memberid733',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole3Player4
        fields = [
            'memberid734',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole3Player5
        fields = [
            'memberid735',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole4Player1
        fields = [
            'memberid741',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole4Player2
        fields = [
            'memberid742',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole4Player3
        fields = [
            'memberid743',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole4Player4
        fields = [
            'memberid744',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole4Player5
        fields = [
            'memberid745',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole5Player1
        fields = [
            'memberid751',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole5Player2
        fields = [
            'memberid752',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole5Player3
        fields = [
            'memberid753',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole5Player4
        fields = [
            'memberid754',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole5Player5
        fields = [
            'memberid755',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole6Player1
        fields = [
            'memberid761',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole6Player2
        fields = [
            'memberid762',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole6Player3
        fields = [
            'memberid763',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole6Player4
        fields = [
            'memberid764',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole6Player5
        fields = [
            'memberid765',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole7Player1
        fields = [
            'memberid771',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole7Player2
        fields = [
            'memberid772',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole7Player3
        fields = [
            'memberid773',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole7Player4
        fields = [
            'memberid774',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole7Player5
        fields = [
            'memberid775',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole8Player1
        fields = [
            'memberid781',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole8Player2
        fields = [
            'memberid782',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole8Player3
        fields = [
            'memberid783',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole8Player4
        fields = [
            'memberid784',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole8Player5
        fields = [
            'memberid785',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole9Player1
        fields = [
            'memberid791',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole9Player2
        fields = [
            'memberid792',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole9Player3
        fields = [
            'memberid793',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole9Player4
        fields = [
            'memberid794',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole9Player5
        fields = [
            'memberid795',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole10Player1
        fields = [
            'memberid7101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole10Player2
        fields = [
            'memberid7102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole10Player3
        fields = [
            'memberid7103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole10Player4
        fields = [
            'memberid7104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole10Player5
        fields = [
            'memberid7105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole11Player1
        fields = [
            'memberid7111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole11Player2
        fields = [
            'memberid7112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole11Player3
        fields = [
            'memberid7113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole11Player4
        fields = [
            'memberid7114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole11Player5
        fields = [
            'memberid7115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole12Player1
        fields = [
            'memberid7121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole12Player2
        fields = [
            'memberid7122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole12Player3
        fields = [
            'memberid7123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole12Player4
        fields = [
            'memberid7124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole12Player5
        fields = [
            'memberid7125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole13Player1
        fields = [
            'memberid7131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole13Player2
        fields = [
            'memberid7132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole13Player3
        fields = [
            'memberid7133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole13Player4
        fields = [
            'memberid7134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole13Player5
        fields = [
            'memberid7135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole14Player1
        fields = [
            'memberid7141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole14Player2
        fields = [
            'memberid7142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole14Player3
        fields = [
            'memberid7143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole14Player4
        fields = [
            'memberid7144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole14Player5
        fields = [
            'memberid7145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole15Player1
        fields = [
            'memberid7151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole15Player2
        fields = [
            'memberid7152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole15Player3
        fields = [
            'memberid7153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole15Player4
        fields = [
            'memberid7154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole15Player5
        fields = [
            'memberid7155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole16Player1
        fields = [
            'memberid7161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole16Player2
        fields = [
            'memberid7162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole16Player3
        fields = [
            'memberid7163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole16Player4
        fields = [
            'memberid7164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole16Player5
        fields = [
            'memberid7165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole17Player1
        fields = [
            'memberid7171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole17Player2
        fields = [
            'memberid7172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole17Player3
        fields = [
            'memberid7173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole17Player4
        fields = [
            'memberid7174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole17Player5
        fields = [
            'memberid7175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole18Player1
        fields = [
            'memberid7181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole18Player2
        fields = [
            'memberid7182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',

            'score2',
    ]


class PLayer3Hole18Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole18Player3
        fields = [
            'memberid7183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole18Player4
        fields = [
            'memberid7184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start7(forms.ModelForm):

    class Meta:
        model = Start7Hole18Player5
        fields = [
            'memberid7185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

    ############## Start 8 ###############


class PLayer1Hole1Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole1Player1
        fields = [
            'memberid811',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole1Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole1Player2
        fields = [
            'memberid812',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole1Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole1Player3
        fields = [
            'memberid813',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole1Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole1Player4
        fields = [
            'memberid814',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole1Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole1Player5
        fields = [
            'memberid815',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole2Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole2Player1
        fields = [
            'memberid821',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole2Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole2Player2
        fields = [
            'memberid822',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole2Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole2Player3
        fields = [
            'memberid823',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole2Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole2Player4
        fields = [
            'memberid824',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole2Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole2Player5
        fields = [
            'memberid825',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole3Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole3Player1
        fields = [
            'memberid831',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole3Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole3Player2
        fields = [
            'memberid832',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole3Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole3Player3
        fields = [
            'memberid833',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole3Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole3Player4
        fields = [
            'memberid834',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole3Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole3Player5
        fields = [
            'memberid835',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole4Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole4Player1
        fields = [
            'memberid841',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole4Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole4Player2
        fields = [
            'memberid842',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole4Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole4Player3
        fields = [
            'memberid843',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole4Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole4Player4
        fields = [
            'memberid844',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole4Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole4Player5
        fields = [
            'memberid845',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole5Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole5Player1
        fields = [
            'memberid851',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole5Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole5Player2
        fields = [
            'memberid852',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole5Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole5Player3
        fields = [
            'memberid853',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole5Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole5Player4
        fields = [
            'memberid854',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole5Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole5Player5
        fields = [
            'memberid855',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole6Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole6Player1
        fields = [
            'memberid861',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole6Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole6Player2
        fields = [
            'memberid862',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole6Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole6Player3
        fields = [
            'memberid863',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole6Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole6Player4
        fields = [
            'memberid864',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole6Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole6Player5
        fields = [
            'memberid865',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole7Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole7Player1
        fields = [
            'memberid871',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole7Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole7Player2
        fields = [
            'memberid872',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole7Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole7Player3
        fields = [
            'memberid873',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole7Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole7Player4
        fields = [
            'memberid874',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole7Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole7Player5
        fields = [
            'memberid875',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole8Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole8Player1
        fields = [
            'memberid881',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole8Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole8Player2
        fields = [
            'memberid882',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole8Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole8Player3
        fields = [
            'memberid883',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole8Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole8Player4
        fields = [
            'memberid884',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole8Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole8Player5
        fields = [
            'memberid885',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole9Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole9Player1
        fields = [
            'memberid891',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
        ]


class PLayer2Hole9Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole9Player2
        fields = [
            'memberid892',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
        ]


class PLayer3Hole9Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole9Player3
        fields = [
            'memberid893',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
        ]


class PLayer4Hole9Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole9Player4
        fields = [
            'memberid894',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
        ]


class PLayer5Hole9Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole9Player5
        fields = [
            'memberid895',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
        ]


class PLayer1Hole10Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole10Player1
        fields = [
            'memberid8101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole10Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole10Player2
        fields = [
            'memberid8102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole10Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole10Player3
        fields = [
            'memberid8103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole10Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole10Player4
        fields = [
            'memberid8104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole10Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole10Player5
        fields = [
            'memberid8105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole11Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole11Player1
        fields = [
            'memberid8111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole11Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole11Player2
        fields = [
            'memberid8112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole11Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole11Player3
        fields = [
            'memberid8113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole11Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole11Player4
        fields = [
            'memberid8114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole11Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole11Player5
        fields = [
            'memberid8115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole12Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole12Player1
        fields = [
            'memberid8121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole12Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole12Player2
        fields = [
            'memberid8122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole12Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole12Player3
        fields = [
            'memberid8123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole12Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole12Player4
        fields = [
            'memberid8124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole12Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole12Player5
        fields = [
            'memberid8125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole13Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole13Player1
        fields = [
            'memberid8131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole13Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole13Player2
        fields = [
            'memberid8132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole13Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole13Player3
        fields = [
            'memberid8133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole13Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole13Player4
        fields = [
            'memberid8134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole13Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole13Player5
        fields = [
            'memberid8135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole14Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole14Player1
        fields = [
            'memberid8141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole14Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole14Player2
        fields = [
            'memberid8142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole14Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole14Player3
        fields = [
            'memberid8143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole14Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole14Player4
        fields = [
            'memberid8144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole14Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole14Player5
        fields = [
            'memberid8145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole15Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole15Player1
        fields = [
            'memberid8151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole15Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole15Player2
        fields = [
            'memberid8152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole15Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole15Player3
        fields = [
            'memberid8153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole15Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole15Player4
        fields = [
            'memberid8154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole15Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole15Player5
        fields = [
            'memberid8155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole16Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole16Player1
        fields = [
            'memberid8161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole16Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole16Player2
        fields = [
            'memberid8162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole16Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole16Player3
        fields = [
            'memberid8163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole16Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole16Player4
        fields = [
            'memberid8164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole16Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole16Player5
        fields = [
            'memberid8165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole17Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole17Player1
        fields = [
            'memberid8171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole17Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole17Player2
        fields = [
            'memberid8172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole17Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole17Player3
        fields = [
            'memberid8173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole17Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole17Player4
        fields = [
            'memberid8174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole17Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole17Player5
        fields = [
            'memberid8175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]


class PLayer1Hole18Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole18Player1
        fields = [
            'memberid8181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
        ]


class PLayer2Hole18Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole18Player2
        fields = [
            'memberid8182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
        ]


class PLayer3Hole18Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole18Player3
        fields = [
            'memberid8183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
        ]


class PLayer4Hole18Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole18Player4
        fields = [
            'memberid8184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
        ]


class PLayer5Hole18Start8(forms.ModelForm):
    class Meta:
        model = Start8Hole18Player5
        fields = [
            'memberid8185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
        ]
        
        
############## Start 9 ###############


class PLayer1Hole1Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole1Player1
        fields = [
            'memberid911',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole1Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole1Player2
        fields = [
            'memberid912',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]

class PLayer3Hole1Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole1Player3
        fields = [
            'memberid913',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole1Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole1Player4
        fields = [
            'memberid914',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole1Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole1Player5
        fields = [
            'memberid915',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole2Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole2Player1
        fields = [
            'memberid921',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole2Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole2Player2
        fields = [
            'memberid922',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole2Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole2Player3
        fields = [
            'memberid923',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole2Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole2Player4
        fields = [
            'memberid924',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole2Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole2Player5
        fields = [
            'memberid925',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole3Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole3Player1
        fields = [
            'memberid931',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole3Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole3Player2
        fields = [
            'memberid932',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole3Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole3Player3
        fields = [
            'memberid933',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole3Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole3Player4
        fields = [
            'memberid934',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole3Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole3Player5
        fields = [
            'memberid935',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole4Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole4Player1
        fields = [
            'memberid941',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole4Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole4Player2
        fields = [
            'memberid942',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole4Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole4Player3
        fields = [
            'memberid943',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole4Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole4Player4
        fields = [
            'memberid944',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole4Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole4Player5
        fields = [
            'memberid945',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole5Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole5Player1
        fields = [
            'memberid951',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole5Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole5Player2
        fields = [
            'memberid952',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole5Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole5Player3
        fields = [
            'memberid953',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole5Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole5Player4
        fields = [
            'memberid954',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole5Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole5Player5
        fields = [
            'memberid955',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole6Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole6Player1
        fields = [
            'memberid961',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole6Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole6Player2
        fields = [
            'memberid962',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole6Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole6Player3
        fields = [
            'memberid963',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole6Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole6Player4
        fields = [
            'memberid964',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole6Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole6Player5
        fields = [
            'memberid965',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole7Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole7Player1
        fields = [
            'memberid971',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole7Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole7Player2
        fields = [
            'memberid972',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole7Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole7Player3
        fields = [
            'memberid973',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole7Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole7Player4
        fields = [
            'memberid974',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole7Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole7Player5
        fields = [
            'memberid975',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]

class PLayer1Hole8Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole8Player1
        fields = [
            'memberid981',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole8Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole8Player2
        fields = [
            'memberid982',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole8Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole8Player3
        fields = [
            'memberid983',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole8Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole8Player4
        fields = [
            'memberid984',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole8Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole8Player5
        fields = [
            'memberid985',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole9Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole9Player1
        fields = [
            'memberid991',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score1',
    ]


class PLayer2Hole9Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole9Player2
        fields = [
            'memberid992',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score2',
    ]


class PLayer3Hole9Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole9Player3
        fields = [
            'memberid993',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score3',
    ]


class PLayer4Hole9Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole9Player4
        fields = [
            'memberid994',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score4',
    ]


class PLayer5Hole9Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole9Player5
        fields = [
            'memberid995',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'hole',
            'score5',
    ]


class PLayer1Hole10Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole10Player1
        fields = [
            'memberid9101',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole10Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole10Player2
        fields = [
            'memberid9102',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole10Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole10Player3
        fields = [
            'memberid9103',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole10Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole10Player4
        fields = [
            'memberid9104',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole10Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole10Player5
        fields = [
            'memberid9105',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole11Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole11Player1
        fields = [
            'memberid9111',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole11Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole11Player2
        fields = [
            'memberid9112',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole11Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole11Player3
        fields = [
            'memberid9113',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole11Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole11Player4
        fields = [
            'memberid9114',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole11Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole11Player5
        fields = [
            'memberid9115',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]


class PLayer1Hole12Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole12Player1
        fields = [
            'memberid9121',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole12Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole12Player2
        fields = [
            'memberid9122',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole12Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole12Player3
        fields = [
            'memberid9123',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole12Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole12Player4
        fields = [
            'memberid9124',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole12Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole12Player5
        fields = [
            'memberid9125',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole13Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole13Player1
        fields = [
            'memberid9131',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole13Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole13Player2
        fields = [
            'memberid9132',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole13Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole13Player3
        fields = [
            'memberid9133',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole13Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole13Player4
        fields = [
            'memberid9134',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole13Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole13Player5
        fields = [
            'memberid9135',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole14Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole14Player1
        fields = [
            'memberid9141',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole14Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole14Player2
        fields = [
            'memberid9142',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole14Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole14Player3
        fields = [
            'memberid9143',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole14Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole14Player4
        fields = [
            'memberid9144',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole14Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole14Player5
        fields = [
            'memberid9145',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole15Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole15Player1
        fields = [
            'memberid9151',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole15Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole15Player2
        fields = [
            'memberid9152',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole15Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole15Player3
        fields = [
            'memberid9153',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole15Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole15Player4
        fields = [
            'memberid9154',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole15Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole15Player5
        fields = [
            'memberid9155',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole16Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole16Player1
        fields = [
            'memberid9161',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole16Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole16Player2
        fields = [
            'memberid9162',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole16Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole16Player3
        fields = [
            'memberid9163',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole16Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole16Player4
        fields = [
            'memberid9164',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole16Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole16Player5
        fields = [
            'memberid9165',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole17Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole17Player1
        fields = [
            'memberid9171',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole17Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole17Player2
        fields = [
            'memberid9172',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score2',
    ]


class PLayer3Hole17Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole17Player3
        fields = [
            'memberid9173',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole17Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole17Player4
        fields = [
            'memberid9174',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole17Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole17Player5
        fields = [
            'memberid9175',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]

class PLayer1Hole18Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole18Player1
        fields = [
            'memberid9181',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score1',
    ]


class PLayer2Hole18Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole18Player2
        fields = [
            'memberid9182',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',

            'score2',
    ]


class PLayer3Hole18Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole18Player3
        fields = [
            'memberid9183',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score3',
    ]


class PLayer4Hole18Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole18Player4
        fields = [
            'memberid9184',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score4',
    ]


class PLayer5Hole18Start9(forms.ModelForm):

    class Meta:
        model = Start9Hole18Player5
        fields = [
            'memberid9185',
            'gameid',
            'firstname',
            'lastname',
            'handicap',
            'handicap18',
            'chgopt9',
            'chpt18',
            'startinghole',
            'score5',
    ]