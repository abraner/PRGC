from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0011_game_format_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensleagueroundscore',
            name='handicap',
            field=models.IntegerField(
                blank=True,
                help_text='Handicap after this round. 18-hole individual gross/net plays from the latest one.',
                null=True,
            ),
        ),
    ]
