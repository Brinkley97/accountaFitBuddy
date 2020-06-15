# Generated by Django 3.0.6 on 2020-06-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190817_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
        migrations.AddField(
            model_name='article',
            name='uploadFile',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]