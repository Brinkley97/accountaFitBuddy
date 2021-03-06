# Generated by Django 2.0.3 on 2019-07-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20190705_0620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='general',
            old_name='author',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='author',
            new_name='username',
        ),
        migrations.AddField(
            model_name='general',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='health',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='general',
            name='group',
            field=models.IntegerField(blank=True, choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='general',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='general',
            name='often',
            field=models.CharField(blank=True, choices=[('1-2', '1-2'), ('3-4', '3-4'), ('5+', '5+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='health',
            name='age',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='health',
            name='height',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='health',
            name='weight',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
