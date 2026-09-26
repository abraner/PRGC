from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0005_golfround_metrics_finalized'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfround',
            name='skins_winners_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='golfround',
            name='closest_pin_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='golfround',
            name='game_format',
            field=models.CharField(
                choices=[
                    ('18_GROSS_NET', '18-Hole Individual Gross/Net'),
                    ('18_HOLE_MENS_LEAGUE', "18-Hole Men's Handicap League"),
                    ('18_IND_CHICAGO', '18-Hole Individual Chicago Points'),
                    ('9_TEAM_CHICAGO', '9-Hole Team Chicago Points'),
                    ('9_WOMENS_LEAGUE', "9-Hole Women's League"),
                    ('9_HOLE_SCRAMBLE', 'Scramble Tournament (9 Holes)'),
                ],
                default='18_GROSS_NET',
                max_length=30,
            ),
        ),
    ]
