import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee=[]
    sleep=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for a in reader:
            coffee.append(float(a["Coffee in ml"]))
            sleep.append(float(a["sleep in hours"]))
    return {"x":coffee,"y":sleep}

def findCorrelation(ds):
    c=np.corrcoef(ds["x"],ds["y"])
    print()
    print(f"The Correlation between the data is: {c[0,1]}")
    print()



def plotGraph():
     with open("chs.csv") as f:
          #creates csv object like the python dictionary
          df = csv.DictReader(f)
          fig = px.scatter(df , x = "Coffee in ml" , y = "sleep in hours")
          fig.show()

def setup():
    dp="chs.csv"
    data=getDataSource(dp)
    
    findCorrelation(data)
    plotGraph()

setup()
# The data is positively correlated.


          
     
     

