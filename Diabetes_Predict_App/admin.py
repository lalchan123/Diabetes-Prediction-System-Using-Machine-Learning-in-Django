from django.contrib import admin
from .models import DiabetesPredict
# Register your models here.
class DiabetesPredictAdmin(admin.ModelAdmin):
    list_display = ('Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome')
    list_filter = ('Outcome',)

admin.site.register(DiabetesPredict,DiabetesPredictAdmin)