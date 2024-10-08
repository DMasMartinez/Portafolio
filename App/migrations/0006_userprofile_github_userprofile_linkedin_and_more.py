# Generated by Django 4.1.5 on 2024-07-15 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_userprofileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileimage',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='App.userprofile'),
        ),
    ]
