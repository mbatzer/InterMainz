# Generated by Django 2.1.1 on 2018-10-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='jersey_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]