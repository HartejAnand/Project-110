import statistics
import pandas as pd
import random
import plotly.graph_objects as go
import csv
import plotly_express as px
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
data=df["number"].tolist()

mean=statistics.mean(data)

def mmean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(30,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=mmean(100)
        mean_list.append(set_of_means)
    fig=ff.create_distplot([mean_list],["averages"],show_hist=False)
    fig.show()


print(mean)
setup()