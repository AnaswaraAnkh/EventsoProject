# Generated by Django 4.2.16 on 2024-10-24 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cameraman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event', models.CharField(blank=True, max_length=300, null=True)),
                ('Phone_Number', models.BigIntegerField(blank=True, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('CAMERAMANLID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cameraman_bookings', to=settings.AUTH_USER_MODEL)),
                ('USERLID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
