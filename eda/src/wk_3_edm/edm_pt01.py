import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder



titanic = pd.read_excel("https://github.com/PinkWink/ML_tutorial/raw/master/dataset/titanic.xls")
le = LabelEncoder()
le.fit(titanic["cabin"])

titanic["gender"] = le.transform(titanic["cabin"])
print(titanic["gender"].head(80))
#corr_titanic = titanic
#corr_titanic["gender"] = corr_titanic["sex"] == "male" 
#corr_titanic.drop(["name", "sex", "home.dest","boat"], axis=1, inplace=True)
#corr_titanic = corr_titanic[corr_titanic.notnull()]
#print(corr_titanic["body"].head(20))
#print(corr_titanic.info())
#print(corr_titanic.corr(numeric_only=True).round(2))
#sns.heatmap(corr_titanic.corr(numeric_only=True).round(2),annot=True, cmap="bwr")
#plt.show()
