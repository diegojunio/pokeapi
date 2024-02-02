# Generated by Django 3.2.23 on 2024-02-02 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_v2', '0014_auto_20231121_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cries', models.JSONField()),
                ('pokemon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemoncries', to='pokemon_v2.pokemon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
