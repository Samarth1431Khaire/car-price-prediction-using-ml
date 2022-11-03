import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report
import pickle

data=pd.read_csv("CAR DETAILS FROM CAR DEKHO1.csv")
print(data)


res=data.isnull().sum()
print(res)

features=data.drop("selling_price", axis="columns")
target=data["selling_price"]

nfeatures=pd.get_dummies(features)

print(features)
print(nfeatures)

x_train,x_test,y_train,y_test=train_test_split(nfeatures,target,random_state=11)




model= RandomForestRegressor(n_estimators=10)
model.fit(x_train,y_train)

s1=model.score(x_train,y_train)
s2=model.score(x_test,y_test)
print(s1)
print(s2)


f=None
try:
     f=open("car.model", "wb")
     pickle.dump(model,f)

except Exception as e:
     print("issue",str(e))
finally:
     if f is not None:
        f.close()

