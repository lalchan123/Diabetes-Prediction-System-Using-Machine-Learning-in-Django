# Generated by Django 3.0.5 on 2021-09-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesPredict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.FloatField()),
                ('Glucose', models.FloatField()),
                ('BloodPressure', models.FloatField()),
                ('SkinThickness', models.FloatField()),
                ('Insulin', models.FloatField()),
                ('BMI', models.FloatField()),
                ('DiabetesPedigreeFunction', models.FloatField()),
                ('Age', models.FloatField()),
                ('Outcome', models.CharField(max_length=50)),
            ],
        ),
    ]
