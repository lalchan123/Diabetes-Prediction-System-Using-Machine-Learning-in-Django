from django.db import models

# Create your models here.
class DiabetesPredict(models.Model):
    Pregnancies = models.FloatField()
    Glucose = models.FloatField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.FloatField()
    Outcome = models.CharField(max_length=50)