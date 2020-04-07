from django.shortcuts import render
from . import ml_model


def home(request):
    return render(request, 'index.html')

def result(request):
    age = int(request.GET["age"])
    sex = int(request.GET["sex"])
    pclass = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = int(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])


    prediction = ml_model.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(request, 'result.html', {'prediction' : prediction})
