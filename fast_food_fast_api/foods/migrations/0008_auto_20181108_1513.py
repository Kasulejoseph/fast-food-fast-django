# Generated by Django 2.1.3 on 2018-11-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20181108_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.SignUp'),
        ),
    ]
