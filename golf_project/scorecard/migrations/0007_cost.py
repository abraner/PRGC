from decimal import Decimal

from django.db import migrations, models


def create_cost_row(apps, schema_editor):
    Cost = apps.get_model('scorecard', 'Cost')
    Cost.objects.get_or_create(
        pk=1,
        defaults={
            'mens_league_18': Decimal('12.00'),
            'gross_net_18': Decimal('6.00'),
            'scramble_9': Decimal('6.00'),
            'team_chicago_9': Decimal('6.00'),
            'womens_league_9': Decimal('6.00'),
            'chicago_18': Decimal('12.00'),
            'golf_course_amount': Decimal('2.00'),
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0006_golfround_skins_and_pin_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mens_league_18', models.DecimalField(decimal_places=2, default=12.0, max_digits=6, verbose_name="18-Hole Men's League cost")),
                ('gross_net_18', models.DecimalField(decimal_places=2, default=6.0, max_digits=6, verbose_name='18-Hole Individual Gross/Net cost')),
                ('scramble_9', models.DecimalField(decimal_places=2, default=6.0, max_digits=6, verbose_name='9-Hole Scramble cost')),
                ('team_chicago_9', models.DecimalField(decimal_places=2, default=6.0, max_digits=6, verbose_name='9-Hole Team Chicago Points cost')),
                ('womens_league_9', models.DecimalField(decimal_places=2, default=6.0, max_digits=6, verbose_name="9-Hole Women's League cost")),
                ('chicago_18', models.DecimalField(decimal_places=2, default=12.0, max_digits=6, verbose_name='18-Hole Individual Chicago Points cost')),
                ('golf_course_amount', models.DecimalField(decimal_places=2, default=2.0, max_digits=6, verbose_name='Golf course amount')),
            ],
            options={
                'verbose_name': 'Cost',
                'verbose_name_plural': 'Cost',
            },
        ),
        migrations.RunPython(create_cost_row, migrations.RunPython.noop),
    ]
