# Generated by Django 4.2.16 on 2024-11-08 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='USERLID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_payment', to=settings.AUTH_USER_MODEL),
        ),
    ]
