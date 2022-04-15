import sqlite3

import pandas as pd
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
def foo(bar):
    print('hello {}'.format(bar))


# Insert into butto on results window page#
with sqlite3.connect('User_Data.db') as db:
    c = db.cursor()
    # validating if the username already exists
find_user = ('SELECT * FROM lefthandvalues WHERE username = ?')
cols = ['id', 'username', 'Force', 'Flex', 'Acceleration', 'date']
c.execute(find_user, ['chuks'])
result = c.fetchall()
df = pd.DataFrame(result, columns=cols)
df=df.tail(5)

df = df.drop(columns=['username', 'date', 'id'])
print(df.head())
df.plot(kind="bar")

plt.title("Left Hand Values")
plt.xlabel("Type of parameter")
plt.ylabel("Values")
str = "lefthand"
plt.savefig(str, dpi=300, bbox_inches='tight')

plotdata = pd.DataFrame({
    "pies_2018": [40, 12, 10, 26, 36],
    "pies_2019": [19, 8, 30, 21, 38],
    "pies_2020": [10, 10, 42, 17, 37]
},
    index=["Dad", "Mam", "Bro", "Sis", "Me"]
)
print(plotdata.head())


from sklearn import tree
dt=tree.DecisionTreeClassifier()
dt.fit(X_train,y_train)
y_pred3= dt.predict(X_test)
print(classification_report(y_test,y_pred3))




