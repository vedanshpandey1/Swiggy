# Generated by Django 4.2.1 on 2023-06-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0005_myuser_user_type_myuser_otp_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='otp_expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
