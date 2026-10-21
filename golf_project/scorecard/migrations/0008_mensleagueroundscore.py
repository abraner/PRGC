from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0007_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensLeagueRoundScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_score', models.PositiveIntegerField()),
                ('played_on', models.DateTimeField()),
                ('golf_round', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mens_league_scores', to='scorecard.golfround')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mens_league_scores', to='scorecard.player')),
            ],
            options={
                'ordering': ['-played_on', '-id'],
            },
        ),
        migrations.AddConstraint(
            model_name='mensleagueroundscore',
            constraint=models.UniqueConstraint(fields=('player', 'golf_round'), name='unique_player_mens_league_round'),
        ),
    ]
