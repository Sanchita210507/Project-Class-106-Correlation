from os import read
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marksInPercent=[]
    daysPresent=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for a in reader:
            marksInPercent.append(float(a["Marks In Percentage"]))
            daysPresent.append(float(a["Days Present"]))
    return {"x":marksInPercent,"y":daysPresent}

def findCorrelation(ds):
    c=np.corrcoef(ds["x"],ds["y"])
    print()
    print(f"The Correlation between the data is: {c[0,1]}")
    print()

def plotGraph():
     with open("MarkList.csv") as f:
          #creates csv object like the python dictionary
          df = csv.DictReader(f)
          fig = px.scatter(df , x = "Days Present" , y = "Marks In Percentage")
          fig.show()

def setup():
    dp="MarkList.csv"
    data=getDataSource(dp)
    findCorrelation(data)
    plotGraph()

setup()
# The data is almost correlated.
        