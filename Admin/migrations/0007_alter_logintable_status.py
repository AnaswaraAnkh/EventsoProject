# Generated by Django 4.2.16 on 2024-11-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_alter_logintable_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Inactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
    ]
