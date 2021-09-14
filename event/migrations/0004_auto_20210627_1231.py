# Generated by Django 3.2 on 2021-06-27 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_suggestionbox'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suggestionbox',
            options={'verbose_name_plural': 'Suggestion Box'},
        ),
        migrations.AlterField(
            model_name='suggestionbox',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.event'),
        ),
    ]
