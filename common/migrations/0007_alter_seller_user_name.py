# Generated by Django 4.1.6 on 2023-02-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_seller_password_seller_user_name_alter_seller_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='user_name',
            field=models.IntegerField(default=0),
        ),
    ]