import statistics
import pandas as pd
import csv 

df = pd.read_csv("class1.csv")
data=df["Marks"].tolist()
opp= statistics.stdev(data)
mean=statistics.mean(data)
print(opp)
print(mean)
