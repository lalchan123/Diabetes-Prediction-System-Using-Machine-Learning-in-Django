from django.shortcuts import render
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sn 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score
from .models import DiabetesPredict
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
    dt = pd.read_csv(r'F:\Project and Thesis\Project\Django Project\ML Django Project\Diabetes Prediction System Using ML in Django\diabetes.csv')
    x = dt.drop('Outcome', axis=1)
    y = dt['Outcome']
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=.30)
    model = LogisticRegression()
    model.fit(xtrain, ytrain)
    if request.method == "POST":
        n1 = float(request.POST['n1'])
        n2 = float(request.POST['n2'])
        n3 = float(request.POST['n3'])
        n4 = float(request.POST['n4'])
        n5 = float(request.POST['n5'])
        n6 = float(request.POST['n6'])
        n7 = float(request.POST['n7'])
        n8 = float(request.POST['n8'])

        pred = model.predict(np.array([n1,n2,n3,n4,n5,n6,n7,n8]).reshape(1,-1))
        result = ""
        if pred == [1]:
            result = "POSITIVE"
        else:
            result = "NEGATIVE"
        
        data = DiabetesPredict(Pregnancies=n1,Glucose=n2,BloodPressure=n3,SkinThickness=n4,Insulin=n5,BMI=n6,DiabetesPedigreeFunction=n7,Age=n8,Outcome=result)
        data.save()
    return render(request, "predict.html",{"result":result,})

def recordData(request):
    data = DiabetesPredict.objects.all()
    paginator = Paginator(data, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "recordData.html",{"page_obj":page_obj, })    