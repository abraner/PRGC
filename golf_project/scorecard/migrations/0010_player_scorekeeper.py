from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0009_womensleagueroundscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='scorekeeper',
            field=models.BooleanField(default=False, verbose_name='Scorekeeper'),
        ),
    ]
