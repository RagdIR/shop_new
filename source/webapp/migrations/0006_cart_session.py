# Generated by Django 2.2 on 2020-09-19 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('webapp', '0005_auto_20200901_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='sessions.Session'),
        ),
    ]