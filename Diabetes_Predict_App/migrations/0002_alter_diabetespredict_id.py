# Generated by Django 3.2.8 on 2021-10-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes_Predict_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetespredict',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
