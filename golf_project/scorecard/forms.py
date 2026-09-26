# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Player, GolfRound, Hole, Squad, HoleScore, PayoutSetting

class MemberRegistrationForm(UserCreationForm):
    # 1. Added role checkboxes
    is_player = forms.BooleanField(
        required=False,
        initial=True,
        label="Register as Player"
    )
    is_captain = forms.BooleanField(
        required=False,
        initial=False,
        label="Register as Captain"
    )

    # 2. Made existing golf fields required=False so non-players can bypass them
    member_id = forms.CharField(max_length=20, label="Member ID", required=False)
    handicap = forms.IntegerField(label="Base Handicap", initial=0, required=False)
    chicago_points_18 = forms.IntegerField(label="18 Hole Chicago Points", initial=0, required=False)
    team_chicago_points_9 = forms.IntegerField(label="9 Hole Team Chicago Points", initial=0, required=False)
    ladies_league_handicap = forms.DecimalField(
        label="Ladies League Handicap",
        max_digits=4,
        decimal_places=1,
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super().clean()
        is_player = cleaned_data.get('is_player')
        is_captain = cleaned_data.get('is_captain')
        member_id = cleaned_data.get('member_id')

        # Rule: If they check Captain, they must also be a Player
        if is_captain and not is_player:
            cleaned_data['is_player'] = True
            is_player = True

        # Validation: If they are a player, make sure they actually provided a Member ID
        if is_player and not member_id:
            self.add_error('member_id', 'A Member ID is required if registering as a Player.')

        return cleaned_data

    def save(self, commit=True):
        # 1. Save the foundational auth User
        user = super().save(commit=commit)

        # 2. Grab checkboxes
        is_player = self.cleaned_data.get('is_player')
        is_captain = self.cleaned_data.get('is_captain')

        # 3. Only build and save the attached Player profile if they are a player or captain
        if is_player or is_captain:
            full_name = f"{user.first_name} {user.last_name}".strip() or user.username

            # Get values safely, defaulting to 0 if empty
            handicap_val = self.cleaned_data.get('handicap') or 0
            cp18_val = self.cleaned_data.get('chicago_points_18') or 0
            tcp9_val = self.cleaned_data.get('team_chicago_points_9') or 0
            ladies_hdcp = self.cleaned_data.get('ladies_league_handicap')

            Player.objects.create(
                user=user,
                name=full_name,
                is_captain=is_captain,  # Saves their captain status to your Player model!
                member_id=self.cleaned_data.get('member_id'),
                handicap=handicap_val,
                chicago_points_18=cp18_val,
                team_chicago_points_9=tcp9_val,
                ladies_league_handicap=ladies_hdcp
            )
        return user


# 🟢 FIXED: Explicitly inherits from forms.ModelForm so Django maps the database class parameters
class ScoringMemberRegistrationForm(forms.ModelForm):
    # 1. Explicit form fields configuration parameters
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label="First Name"
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label="Last Name"
    )

    # Role Checkbox
    is_player = forms.BooleanField(
        required=False,
        initial=True,
        label="Register as Player"
    )

    # 9-Hole handicap placeholder field
    handicap_9_hole = forms.IntegerField(
        required=False,
        initial=0,
        label="9 Hole Handicap"
    )

    # 2. FORCE SYSTEM ROW ORDERING TO THE TOP
    field_order = [
        'first_name',
        'last_name',
        'is_player',
        'is_captain',
        'handicap',
        'handicap_9_hole',
        'chicago_points_18',
        'team_chicago_points_9',
        'ladies_league_handicap'
    ]

    class Meta:
        # 🟢 CRITICAL FIXED LINK: Explicitly binds this ModelForm straight to your Player database table row!
        model = Player
        fields = [
            'is_captain',
            'handicap',
            'chicago_points_18',
            'team_chicago_points_9',
            'ladies_league_handicap'
        ]
        labels = {
            'is_captain': 'Register as Captain',
            'handicap': '18 Hole Handicap',
        }

    def clean(self):
        cleaned_data = super().clean()
        is_player = cleaned_data.get('is_player')
        is_captain = cleaned_data.get('is_captain')

        # Rule: If they check Captain, they must also be a Player
        if is_captain and not is_player:
            cleaned_data['is_player'] = True

        return cleaned_data

    def save(self, commit=True):
        player = super().save(commit=False)

        # Combine inputs to write straight into your model's 'name' column
        first = self.cleaned_data['first_name'].strip()
        last = self.cleaned_data['last_name'].strip()
        player.name = f"{first} {last}"

        # Guarantee user is left empty to bypass auth_user table mapping limits
        player.user = None

        if commit:
            player.save()
        return player






class ManualSquadForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=Player.objects.filter(is_playing_today=True),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Players for this Squad"
    )

    class Meta:
        model = Squad
        # Keeps the exact database model field names to stop FieldError crashes,
        # while keeping 'squad_number' removed for automatic background generation.
        fields = ['starting_hole', 'scorekeeper']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Look up the active golf round configuration
        active_round = GolfRound.objects.filter(is_active=True).first()

        # 2. Base query: must be marked as playing today
        available_players = Player.objects.filter(is_playing_today=True)

        if active_round:
            # 3. Exclude players who are already tied to a squad in this active round
            assigned_ids = Player.objects.filter(squads__round=active_round).values_list('id', flat=True)

            # 🟢 FIXED: Changed 'assigned_pattern' to 'assigned_ids' to permanently fix the NameError crash
            available_players = available_players.exclude(id__in=assigned_ids if assigned_ids.exists() else [])

        # 4. Assign the filtered datasets back to the input widgets dynamically
        self.fields['players'].queryset = available_players.order_by('name')
        self.fields['scorekeeper'].queryset = available_players.order_by('name')
        self.fields['starting_hole'].queryset = Hole.objects.all().order_by('hole_number')

        # Re-labels the field text on screen to read "Designated Captain" natively!
        self.fields['scorekeeper'].label = "Designated Captain"






# Open scorecard/forms.py and update your PayoutRulesForm to look exactly like this:
class PayoutRulesForm(forms.ModelForm):
    class Meta:
        model = PayoutSetting
        # FIXED: Removed 'skins_winners' and 'kp_winners' completely from this fields array list
        fields = ['entry_fee', 'course_cut_per_player', 'specialty_pot_percentage']
        labels = {
            'entry_fee': 'Entry Fee ($ per Player)',
            'course_cut_per_player': 'Golf Course Cut ($ per Player)',
            'specialty_pot_percentage': 'Skins & KP Pot (% of Remainder)'
        }


