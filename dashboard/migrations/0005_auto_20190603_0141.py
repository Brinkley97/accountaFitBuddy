# Generated by Django 2.0.3 on 2019-06-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_healthdata_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthdata',
            old_name='lastName',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='healthdata',
            name='firstName',
        ),
        migrations.AddField(
            model_name='healthdata',
            name='first_name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='healthdata',
            name='last_name',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
